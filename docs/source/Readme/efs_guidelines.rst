.. _efs_guidelines:

EFS Guidelines
--------------

This document gives guidelines on EFS documents creation.


**Templates**

:ref:`use_case_template` or :ref:`ac_template` shall be used for UC and AC EFS documents respectively.


**General remarks**

* Each document should start with a unique label.

* Filename should match document's label.


**Descriptions**

* Use numbered lists for steps of the use case and acceptance criteria.

* Use sub-numbering for optional and alternative scenarios.

* If a step is too complicated, it can be extracted to a separate page and referenced.

* Literal blocks are by default formatted as C++ code. You can disable syntax highlighting in the document by adding ::

    .. highlight:: none

  somewhere before the first literal block.


**Diagrams**

* Name all of your diagrams.

* List all actors at the beginning of the diagram to control their order.

* Use solid lines for function calls and message exchange.

* Use dashed lines only for function returns. Do not use the *<return>* keyword.

* Use `rnote` elements to describe component behaviour.

* User `hnote` elements to describe component state (preconditions and postconditions).

* Keep your diagrams small. Don't be afraid to split your diagrams and use references if they become too large.

.. uml::

    @startuml
    Title
        Diagram title
    End title

    box
        participant "Foo Bar"
    end box

    participant Baz

    hnote over "Foo Bar": Precondition

    "Foo Bar" -> Baz: functionCall()
    rnote over Baz: verify arguments
    rnote over Baz: compute result

    return true
    'above is equivalent to: Baz --> "Foo Bar": true

    ...

    "Foo Bar" -> Baz: FOO_BAR_REQ_MSG
    ref over "Foo Bar", Baz: Message processing
    Baz -> "Foo Bar": FOO_BAR_RESP_MSG

    hnote over Baz: Postcondition

    @enduml

.. uml::

    @startuml
    Title
        Message processing
    End title

    box
        participant "Foo Bar"
    end box

    participant Baz

    note over "Foo Bar", Baz: Message processing details\non a separate diagram

    @enduml


**References**

* Use references where appropriate.

* List all references in the *References* section at the bottom of the document.

* If two references have the same name (e.g. :ref:`UWEM_BE_IWF_UC_AccessTokenRequest` and :ref:`UWEM_BE_IWF_UC_AccessTokenRequest_ui_agent_ac`), add a short description after each.


**How to generate files for review**

.. highlight:: none

* Generate HTML documentation::

    ./init_linux.sh
    . virtualenvs/sphinx/bin/activate
    sphinx-build -j auto -b html source build/html FILENAMES...

* Open generated documentation in Google Chrome and print to PDF


**How to post a review**

* `Create a collaborator account`_ if you have not already done it
* `Open Collaborator`_ and create a new review
* Provide a descriptive name for the review; add a feature prefix (e.g. [5GC001521])
* Set the template to Nokia Light Review
* Set the deadline
* Write an overview
* Choose your country and site
* Provide product name (e.g. Air Scale Indoor)
* Specify the release (e.g. 5G19B)
* Provide comments due date. Set it to a date earlier than the deadline
* Provide feature ID (the same as the review name prefix)
* Add participants:

  - add yourself as the author
  - for AC reviews, add Piotr Bienkowski and Sylwia Nawoj as reviewers
  - for UC reviews, add Bogdan Orzechowski, Michal Wiatr, Wojciech Gazda and Piotr Bienkowski as reviewers
  - add relevant observers

* Upload PDF files
* Move review to inspection phase

  - if you choose 'Nokia controlled review' then you must add 'Moderator' to the review
  - click on 'Inspection' button 

.. _`Create a collaborator account`: https://nsnsi.service-now.com/ess?id=sc_cat_item&sys_id=022a1c254fd03a40ac5c4c318110c7a5
.. _`Open Collaborator`: https://collab.int.net.nokia.com/ui
