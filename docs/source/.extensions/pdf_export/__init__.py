from sphinx.application import Sphinx
import os
import shutil
import glob
import pdfkit

html_pdf_paths = []


def generate_pdf_path(app: Sphinx, pagename):
    pdf_root = app.config.pdf_root_path
    host = app.config.host

    if not pdf_root:
        pdf_root = '/'.join([os.getcwd(), 'pdf'])
        
    html_path = '/'.join([app.outdir, *pagename.split()]) + '.html'
    pdf_path = '/'.join([pdf_root, *pagename.split()]) + '.pdf'
    target_path = '/'.join([host, 'pdf', *pagename.split()]) + '.pdf'

    html_pdf_paths.append((html_path, pdf_path))
    return target_path


def add_pdf_download_button(app, pagename, templatename, context, doctree):
    if 'FN' in pagename or 'UC' in pagename:
        path = generate_pdf_path(app, pagename)

        context['get_pdf_button_enabled'] = True
        context['get_pdf_button_html_code'] = f'''
            <div class="wy-dropdown wy-dropdown-left float-right">
            <form method="get" action="{path}" target="_blank">
                <button type="submit" class="btn">
                <i class="fa fa-download"></i> Get PDF</button>
            </form>
            </div>
            '''.strip()
    else: 
        context['get_pdf_button_enabled'] = False


def generate_pdf(app, exception):
    options = {'page-size': 'A3', 'margin-top': '0in', 'margin-right': '0in', 'margin-bottom': '0in', 'margin-left': '0in'}

    for html_path, pdf_path in html_pdf_paths:
        ensure_dir(pdf_path)
        pdfkit.from_file(html_path, pdf_path, options=options)


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def setup(app): 
    app.add_config_value('pdf_root_path', '', 'html')
    app.add_config_value('host', '', 'localhost')

    html_pdf_paths.clear()

    app.connect('html-page-context', add_pdf_download_button)
    app.connect('build-finished', generate_pdf)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
        }