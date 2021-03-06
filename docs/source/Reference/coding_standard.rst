.. _header-n0:

Coding Standard
===========================

.. _header-n3:

MUST-HAVE rules
---------------

-  Align code with the formatting described in the standard. Spaces must
   be used instead of tabs for indentation. Block brackets {} must be
   placed in the next line at the same level of indentation, i.e. shall
   follow the Allman specification.

-  Do not use using namespace in header files.

-  Do not use following #ifdefs as: #ifdef UT, #ifdef SCT, #ifdef 0
   (same for #ifndef).

-  Members in class have to conform to order listed in this Standard.
   Refer to chapter 3.2 for details.

-  For any class with virtual methods or any base class destructor
   should be marked as virtual.

-  Do not use memcpy for non-POD structures.

-  Use standard library as much as possible. When looking for
   functionality you should look for it in following order: std, boost,
   ccs, implement it by yourself.

-  Avoid using raw pointers to indicate memory ownership. Refer to
   chapter 7.8 for details.

-  Do not use name prefixes.

-  Never check for NULL after allocation with new keyword, don’t use new
   (no throw).

-  When using functions which may throw an exception, always consider
   whether it is possible that the function will throw and if so, take
   steps to handle it to avoid application termination.

-  For system calls use dedicated classes instead of directly executing
   commands. Thanks to this your code will be easier to test (refer to
   7.7 for details).

-  Unit Test shall run in less than 100 ms.

-  Unit Test shall test 1 class only and be small enough to help you
   localize problems when it fails.

-  Do not declare multiple variables in one line.

.. _header-n36:

GOOD PRACTICE rules
-------------------

-  Formatting tool shall be added to each repository along with
   configuration file. It is preferred that each developer runs the tool
   before making code public, either via commit or before publishing
   diff.

-  Do not create new macros.

-  Use enum class for new enums.

-  If you are overriding method, use override keyword.

-  Use #pragma once instead of include guards.

-  Preserve appropriate order of includes (see chapter 6.1.5 for
   details).

-  Use static for members, methods and globals where applicable.

-  Use const for input parameters, methods, local variables and data
   members where applicable.

-  Use angled brackets <> for std includes, everything else shall be put
   in “”.

-  Use using namespace in source files only when necessary, in smallest
   scope possible.

-  Prefer Copy constructor/dedicated methods instead of memcpy.

-  If you do not need some code, remove it instead of commenting it out.
   When you see commented out code – remove it.

-  When writing code, have a saying “premature optimization is a root of
   all evil” in mind. Treat code more like a human readable
   documentation rather than a set of instructions.

-  Avoid out parameters – prefer returning value.

-  Header files are not designed to save you from typing. Avoid common
   includes files. Include only what you need.

-  Avoid creating functions longer than 20 lines.

-  When hardcoded value is not self explanatory enough, consider a named
   constant.

-  Put standalone global functions into namespaces, with exception for
   functions which have to be in the global namespace, operators and
   specific overloads.

.. _header-n74:

Introduction
------------

It is always reasonable to encourage consistency of coding style.
Application of the Scrum methodology, however, places a higher level of
importance that there is consistency across code-bases, because lack of
such consistency steepens the learning curve associated with moving
developers from one system component to another. Keeping the code and
design consistent is crucial for fast introduction of new features.

The coding standard goes beyond just consistency – it sets out
recommendations for good practice.

.. _header-n77:

Scope
~~~~~

Rules described in this document apply to all source code belonging to
MBB Small Cell project, regardless if they are new, inherited or just
old. It is developer’s responsibility to keep source code aligned with
coding standard during normal workflow. E.g. when one encounters an old,
outdated code, it should be made compliant to this guideline before
starting feature implementation.

Recommendations should be followed as much as possible, however
additional design rules are more of a guideline – code should conform to
them, but if there are reasonable concerns about the default solution,
developer is free to do the implementation in their own way. That being
said, such a decision must be well documented so other people will not
try to “fix” the code and encounter the same problems which resulted in
abandoning the default approach.

.. _header-n80:

Enforcement
~~~~~~~~~~~

Rules are strong coding requirements and must be followed by all
developers within the project team. The compliance with rules is
mandatory.

Breaking rules is allowed for good reasons only and must be clearly
documented in the code (comment). The non-compliance also must be
accepted by every code reviewer.

Some rules and recommendations of this guide will be implicitly checked
by tools like Klocwork. However, many rules cannot be checked
automatically. This task is left to code reviews.

.. _header-n84:

Naming
------

.. _header-n85:

Files
~~~~~

Extensions for C++ headers files shall be .h, for source files use .cpp
extension. For C, extensions are .c and .h. Note that C headers should
include #ifdef \__cplusplus extern "C" sections. If header does not
provide this, consider wrapping it into a .h file with structure as in
listing.

.. code:: cpp

   #ifdef __cplusplus
   extern "C"
   {
   #endif

   #include "foo.h"

   #ifdef __cplusplus
   }
   #endif

Files should not be prefixed with system component name.

To avoid name clashes, additional prefixes might be needed. In such
case, additional prefixes shall follow camel case naming.

The file name should reflect its content, i.e. should contain at least
one class named as the file name.

.. _header-n91:

#pragma once
~~~~~~~~~~~~

All header files shall include #pragma once directive in order to
prevent multiple inclusion of the same header file at compile time. Do
not use header guards for the same purpose.

.. code:: cpp

   #pragma once
   /* ... */

.. _header-n94:

Namespaces
~~~~~~~~~~

Namespace names follow the same naming convention as functions, i.e.
camelCase. Namespace bodies shall not be indented. Components which
compile to executable, for example CellP or DspProxy, should not have
their own root namespace. Library code, for example PIL, libOM_utils,
should all be located in some root namespace – e.g. PIL should have pil
namespace, and utils should be in omUtils, in order to allow easier
naming and avoid conflicts in library code. Prefer flat namespaces;
having nested directories is fine, but there should not be nested
namespaces, unless to hide it from possible users of the code.

.. code:: cpp

   namespace enbc
   {
   namespace serverManager
   {
   class IdManagement
   {
   /* ... */
   };
   }
   }

Namespace aliases and using directives are allowed only in source code
files. It is forbidden to put them globally into header files, do not
use using namespace there as it pollutes global namespace. An exception
are unit test source files where making a using statement for ::testing
namespace or its members is allowed.

Namespace aliases should refer to global scope, starting with ::.

.. code:: cpp

   void foo()
   {
       namespace fsm = ::common::fsm;
       using namespace std;
       for (vector<fsm::Event>::iterator i /* ... */)
       {
       }
   }

These rules does not include using in contex of creation type alias
(refer chapter 6.7)

.. _header-n101:

Types
~~~~~

Type names should start with capital letter (UpperCamelCase). Acronyms
like SampleRrdType should be avoided, but are allowed.

Naming rules apply to all user-defined types, including enumerations,
nested types, template parameters and so on. When an acronym has to be
used, it is appropriate to only use upper case letter for first letter
in the acronym, such as Rdd instead of RDD.

As an exception, types that have the same semantics as types defined in
standard library should have names conforming to STL acronym naming
convention. This applies especially to iterator, const\ *iterator and
value*\ type defined for custom containers. This is required by STL, in
order to enable standard algorithms and iterators to work on
user-defined types.

Types or variable names should not suggest the underlying structure type
(e.g. list, array, map) unless they actually implement a list or an
array, etc. Plural form can be used instead or at most generic hint like
container or collection. Typedefs are an exception to these rules, as
they define an alias, rather than a new type.

.. code:: cpp

   typedef Type OtherType;
   typedef std::vector<UeId> UeIdsVector;

   struct Structure
   {
   };

   class Class
   {
   public:
       Class();
       ~Class();

   private:
       int privateField;
   };

   template <typename Something>
   class Template
   {
   public:
       typedef Something Type;
   };

   class LinkContainer;
   class PciToResolveList; // discouraged

   class PcisToResolve; // recommended

.. _header-n107:

Enumerations
~~~~~~~~~~~~

Enumerated type name should follow naming convention of other types. For
new enums always use enum class introduced by C++11. This eliminates the
name conflict issue associated with the C++98 enums.

.. code:: cpp

   enum class MyEnum
   {
       Foo,
       Bar,
       Qux
   };

.. _header-n110:

Functions
~~~~~~~~~

Function names should begin with a small letter. Generally, the first
word of the function name should be a verb, although generic verbs like
”do”, ”perform”, ”process” etc. should be avoided, but can be used as a
prefix (e.g. processScheduledJobs). This applies to methods, static
methods and free functions as well.

`Meaningful naming for functions has been discussed on this wiki
page. <https://bts.inside.nokiasiemensnetworks.com/twiki/bin/view/LTEeNB/CommonReviewPrinciples#MeaningfulNaming>`__

Following generic naming recommendations should be applied:

-  For classes and function names: the bigger the scope, the shorter the
   name should be (more generic),

-  For variables: the bigger the scope, the longer the name should be
   (more descriptive).

.. code:: cpp

   class Observer
   {
   public:
       virtual ~Observer() {}
       virtual void update() = 0;
   };

   class LinkEstablishmentObserver : public Observer
   {
   public:
       virtual void update() override
       {
         foo();
       }
   };

   class UeLoadBalancer
   {
   public:
       void bar();
   private:
       void chooseUesForPushingOutOfCellByItsPriority();
   };

   std::vector<UeId> ueIdsReservedForAllocationsDueToCollisions;

   void updateAllUesWithValue(Value v)
   {
       for (int i = 0; i < 10; ++i)
       {
           myObject[i].setValue(v);
       }
   }

“Begin with a verb” recommendation does not apply to standard names
taken from STL, like ``begin()``, ``empty()``, etc. In this case
semantics must be exactly the same as defined in standard library,
including const and ``throw()`` constraints.

.. code:: cpp

   class Container
   {
   public:
       class iterator;
       iterator begin();
   };

.. _header-n123:

Variables and parameters
~~~~~~~~~~~~~~~~~~~~~~~~

Variable names shall follow lower camel case notation for both const and
non-const. Acronyms in variables names shall also follow camel case
(e.g. lockBtsomDelta instead of lockBTSOMDelta).

Adding a variable to a large, existing set of variables – in that case a
local naming convention might be applied: Variable names shall not be
prefixed with scope information. Do not use: p\ *, m*, l\_, ptr, or any
other name prefixes.

Postfixing or prefixing variable name with type information (so-called
Hungarian notation) is not permitted, as it is considered harmful from
maintenance point of view and is not needed in strongly typed languages
like C++. This restriction includes shortened Hungarian notation, with
prefixes for pointer and reference types (e.g. rReference or pPointer).
Variable names should not suggest their underlying structure, e.g. list,
array, map.

.. code:: cpp

   const char* globalConstCStyleString = “some value”;

   struct Structure
   {
       int publicField;
   };

   class MyClass
   {
   public:
       int getField() const;
       void setField(int value);
       int publicField; // discouraged

   private:
       int privateField; // recommended!
       int* counterPtr; // discouraged
       std::list<int> numberList; // discouraged
       std::list<int> numbers; // recommended!
   };

   MyClass globalObject; // permissible, although global objects are discouraged

   int function(int formalArgument)
   {
       int localCopy = formalArgument;
       return localCopy;
   }

.. _header-n128:

Macros
~~~~~~

Macros shall be avoided where possible. Macro names shall consist of all
capital letters and shall include component prefix. Macro arguments
shall follow the same naming convention as functions’ arguments.

Local macros shall be undefined as soon as possible. It is also advised
to produce compilation error when multiple definitions occur.

Multi-statement macros should be encased in do { } while(0) blocks to
avoid errors in if else blocks. For improved readability, backslashes
should be aligned to right.

.. code:: cpp

   #ifdef ENBC_MACRO
   #error ENBC_MACRO already defined!
   #else
   #define ENBC_MACRO(function, argument) \
       do \
       { \
           somePrefix##function(argument); \
       } while (0)
   #endif
   ENBC_MACRO(foo, " bar");
   #undef ENBC_MACRO

.. _header-n134:

Templates
~~~~~~~~~

Templates shall be named in the same convention as standalone types.
Template parameters shall be named the same as types, regardless if they
are type or non-type parameters. Prefer declaring type parameters with
typename keyword over class (both forms are allowed, though).

.. _header-n136:

Definition in source file or header file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When deciding whether method definition should go to source or header,
main rule to follow is consistency. In presence of source file
corresponding to the header, all method definitions should go to that
source file.

Header-only classes are allowed and should have a .h extension as any
other header.

.. _header-n139:

Formatting
----------

Consistent code formatting helps during merging and patching the code.
For this purpose there were created tool to make formatting
consistent[Formatter]. Code need to be formatted as it would be
formatted by tool. It is advised to make change sets as small as
possible (including formatting changes) so they can be easily examined.
Therefore developers should disable extensive automatic code
reformatting in their tool of choice.

If the file requires extensive reformatting, it should be done as a
separate check-in in CM tool, before starting actual implementation.
This is to avoid difficult merging and patching.

.. _header-n142:

Indentation and whitespace
~~~~~~~~~~~~~~~~~~~~~~~~~~

Tabs are forbidden, code shall be indented with 4 spaces per level. Do
not put white space characters at the end of line. Single whitespace
shall be added before opening parenthesis in control statements like if,
for, while, catch or switch. Do not put whitespace before opening
parenthesis when declaring or calling a function, or constructing an
objectFormatting should conform rules defined in .clang-format file.

.. code:: cpp

   void foo()
   {
   ····// 1st level
   ····if (...)
   ····{
   ········bar(); // 2nd level
   ····}
   ····myFunction(param1, param2);
   ····MyClass object(param3);
   }

Functions and control statements with long parameter lists should be
indented with spaces either up to opening brace or, in case of a long
function name, with parameters in separate lines, as presented in the
example below. Also, one might want to keep formal parameters’ names in
one column.

When dealing with long expressions, break the line before the operator,
so next lines begin with one. When dealing with bool operators, surround
complex predicates in parentheses to avoid ambiguity.

As a general rule, try to keep lines below 110 characters. The rationale
is:

-  Makes it is easier to print the code,

-  makes it is easier to do 2-pane diff,

-  other people’s IDE (acronym) panels would not cover the text.

.. code:: cpp


   void foo(const ArgumentOne &argument1,
   ·········const ArgumentTwo &argument2,
   ·········const ArgumentThree &argument3,
   ·········const ArgumentFour &argument4,
   ·········const ArgumentFive &argument5)
   {
   ····SomeValue& value = foo.getBar().getQux();
   ····if (!value.empty() && value[0] == 5 && predicate3)
   ····{
   ········doSomething();
   ····}
   }

   void veryLongAndDescriptiveFunctionName(
   ····const ArgumentOne &argument1,
   ····const ArgumentTeo &argument2)
   {
   ····handleMessage();
   }

.. _header-n156:

Classes and constructors
~~~~~~~~~~~~~~~~~~~~~~~~

Initialization lists in constructors shall begin on a new line with
indented colon. When initialization list does not fit in one line, each
initialization should be written on a separate line:

.. code:: cpp

   Foo::Foo(int initializer)
   ····: firstMember(initializer),
   ······secondMember(initializer),
   ······thirdMember(initializer + 1),
   ······fourthMember(initializer + 2),
   ······fifthMember(initializer + 3),
   {
   }

When initialization list does fit in single line, it is fine to put all
initialization in same line:

.. code:: cpp

   Foo::Foo(int initializer) : firstMember(initializer), secondMember(initializer)
   {
   }

..

   Listing 14. Initialization list formatting – with short
   initialization list.

A class definition should start with its public: section, followed by
its protected: section and then its private: section. If any of these
are empty, omit them.

Within each section, member declaration should appear as in stated
below:

-  enums,

-  nested types, typedefs, usings,

-  static const data members,

-  constructors,

-  destructor,

-  methods,

-  data members (except static const data members).

There is one exception – friend declarations should always be in the
private section on the beginning of the class:

.. code:: cpp

   class Foo : public boost::noncopyable
   {
       friend class Other;
   public:
       class iterator
       {
           // ...
       };

       Foo();
       ~Foo();

       void foo();
       int publicVariable; // discouraged

   protected:
       void bar();
       int protectedVar; // discouraged

   private:
       typedef til::Holder<int> Holder;
       Holder member;
   };

.. _header-n184:

Blocks
~~~~~~

Opening and closing braces shall have the same level of indentation and
should be placed in the next line. Presence of braces in one liners is
not obligatory, when in doubt whether braces improve readability in
particular case just add them.Do not use comments to mark end of blocks
such as //end if.

.. code:: cpp

   class Class
   {
   public:
       int getInt() const
       {
           return int;
       }

       bool someOtherStuff();
   };

   bool Class::someOtherStuff()
   {
       try
       {
           if (getInt() == 0)
           {
               bool returnValue = false;
               // some logic follows...
               return returnValue;
           }
           else
           {
               return false;
           }
       }
       catch (const std::exception &)
       {
           // some exception handling
       }
   }

   int getFive()
   {
       return 5;
   }

.. _header-n188:

Loops and control statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Switch statements shall be formatted like below. Try to avoid long
switch tables as they are very hard to maintain. Presence of default
section depends on the use case – when all values of an enum are to be
covered, then default shall be omitted, as on addition of new case this
will result in compilation warning. Add default case only when we
intentionally do not cover all cases.

The above applies when we are switching based on ‘enum’ type. On value
types, always include default section.

By default, all switch cases should include break statement; this of
course does not apply to switch-based conversion functions, where every
case is followed by immediate return or throw/assert statement.

Avoid fall-through cases; it’s allowed only for cases without code.

.. code:: cpp

   int convertEnumAToInt(EnumA value) // static check - compilation warning
   { // on missing case label
       switch (foo)
       {
           case Foo::A:
               bar();
               break;
           case Foo::B:
           case Foo::CC:
               qux();
               break;

           // note lack of default statement!
       }

       throw std::logic_error("Unknown Foo");
   }

   int convertEnumAToInt(EnumA value) // runtime check - will result in exception in
   { // case of unexpected enum value
       switch (value)
       {
           case EnumA::128:
               return 128;
           case EnumA::256:
               return 256;
           default:
               // both cases listed below are valid and depend upon use case:
               throw std::logic_error("Unknown EnumA");

               // OR
               // return 1;
       }
   }

Generally, for and while loops should be preferred over do while.
Iterators should have a meaningful name. C++11 provides for ( : )
syntax, which is preferred when working with containers; sometimes for
vectors indexed loops are better.

Loop statements shall be formatted with keywords on separate lines, as
follows:

.. code:: cpp

   while (predicate && otherPredicate)
   {
       foo();
   }

   // do-while loops should be avoided
   do
   {
       foo();
   } while (predicate);

   for (ClassName::iterator i = container.begin(); i != container.end(); ++i)
   {
       for (const Type& item : container) // C++11 range-based for loop
       {
           foo(item);
       }
   }

.. _header-n197:

Comments
--------

Comments should be only used in appropriate situations. The best code is
self-documenting – focus rather on meaningful names rather than on
obvious comments.

When delivering code having dependency on another, not yet delivered
code, following code convention should be used:
[LTExxxx/LBTxxxx/Internal] TODO: reason, e.g.

.. code:: cpp

   // [LTE2464] TODO: uncomment when BM updates Info Model

.. _header-n201:

Logging program execution
~~~~~~~~~~~~~~~~~~~~~~~~~

There are few functions/macros to make logs unified. The best way to log
program execution is using stream oriented API defined in file:
``C_Application\SC_OAM\OM_Common\Include\BtsOmLogStream.h``. The
benefits from using stream oriented API are:

-  It’s type safe (as opposed to printf based solutions);

-  It’s easier to use (you don’t need to know if type is unsigned or not
   and it’s size);

-  It’s easier to print complicated structures (one can define
   ``operator<<`` for printing structures, enums and other types);

Additionally it’s prints also source file where log is located and it
makes easier to analyse log.

.. _header-n211:

Assertions
----------

.. _header-n212:

Use compile-time assertions instead of run-time assertions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compile-time assertions or static assertions might prolong compilation
times, but improve run-time performance and reduce code complexity.
Further on compile-time assertions do not depend on code coverage and
are always guaranteed to be tested. So whenever failure conditions are
invariable, i.e. already testable at compile time, let the compiler do
the work for you.

.. code:: cpp

   static_assert(65535 > sizeof(MyMsg));
   AaSysComMsgCreate(MY_MSG_ID, sizeof(MyMsg), destination);

.. _header-n215:

Never use assert()
~~~~~~~~~~~~~~~~~~

When the expression passed as argument to assert() evaluates to false, a
message is written to the standard error device and abort is called to
terminate the application. In the context of BTSOM System Components,
messages written to standard error device do not get written to syslog
and thus are lost. Calling abort() raises a SIGABORT signal, being
handled in the CCS default signal handler. The call stack printed to
syslog before terminating does not include the location of the failing
assert(), but stops at the CCS signal handler. Thus a failing assert()
will leave no trace behind in syslog of the original cause for the
failing assert(). Only the SIGABORT signal and earlier logs will give a
hint that an assert() might have failed and what might have happened. As
NDEBUG is not defined for Release Builds this is not acceptable in the
field, but even in early test phases diagnosing failed assert() calls is
not straightforward. Thus usage of assert() is not allowed.

.. _header-n217:

Never use AaErrorAssert()
~~~~~~~~~~~~~~~~~~~~~~~~~

By macro AaErrorAssert() CCS provides an assertion macro that overcomes
the drawbacks of aforementioned standard assertion macro assert(). When
the expression passed to AaErrorAssert() evaluates to false, then the
failing expression and the complete call stack is written to syslog and
the application is aborted.

``AaErrorAssert()`` can be removed from executable at compilation time
by defining AAERROR\ *ASSERTION*\ DISABLED. As
AAERROR\ *ASSERTION*\ DISABLED is defined in all projects for release
builds, thus AaErrorAssert() is only present and effective for debug
builds. To avoid undefined behaviour in the field, removing such
assertions for release builds requires 100% scenario coverage when
testing debug builds, which cannot be guaranteed. It was even seen that
CI SCT regression (using release builds) passed, whereas SCT regression
on host (using debug builds) failed. This can only be explained by some
developers either running SCT regression for release builds or
committing without regression testing. To close these loopholes usage of
AaErrorAssert() is not allowed.

.. _header-n220:

Never use assertions where error handling is feasible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every failing assertion causes a break in service availability and thus
impacts customer’s and consequently NSN’s revenue. Thus never use
assertions where error handling is feasible and service execution can
continue without any side effects.

Do not assert any data received over external interfaces. In such cases
error handling needs to take place. Interfaces to other system
components within OAM are considered to be extern.

.. _header-n223:

C++ Features
------------

.. _header-n224:

Classes
~~~~~~~

.. _header-n225:

class vs. struct
^^^^^^^^^^^^^^^^

Use a struct only for passive objects that carry data; everything else
is a class. The struct and class keywords behave almost identically in C++. We add
our own semantic meanings to each keyword, so you should use the
appropriate keyword for the data-type you're defining. Structs should be used for passive objects that carry data, and may have
associated constants, but lack any functionality other than
access/setting the data members. The accessing/setting of fields is done
by directly accessing the fields rather than through method invocations.
Methods should not provide behavior but should only be used to set up
the data members, e.g., constructor, destructor, initialize(), reset(),
validate().

If more functionality is required, a class is more appropriate. If in
doubt, make it a class.

.. _header-n230:

Interfaces
^^^^^^^^^^

Developers should pay extra care to create well-defined interfaces. It
is strongly recommended not to inherit from any concrete classes
containing complete implementation; when creating interfaces you should
follow ISP (Interface Segregation Principle). The destructor of an interface class shall be declared virtual and have
an empty implementation (see example below). A protected empty implementation of assignment operator is preferred in
order to prevent object slicing. Consider deriving from boost::noncopyable, as most classes inheriting
from interfaces should not be copyable. If you need copies, consider
adding a clone() method.

.. code:: cpp

   namespace oam
   {

   class IdManagement : private boost::noncopyable
   {
   public:
       virtual ~IdManagement()
       {
       }

       virtual void handleMessage(message::IdAllocationReq* message) = 0;
   protected:
       IdManagement &operator=(const IdManagement&)
       {
           return *this;
       }
   };

   }

.. _header-n236:

Abstract base classes
^^^^^^^^^^^^^^^^^^^^^

Abstract base classes are sometimes useful and can provide means for
much clearer implementation with an example of template method pattern.
They are also useful when it comes to remove duplication in some cases.

.. _header-n238:

Deriving from base classes
^^^^^^^^^^^^^^^^^^^^^^^^^^

When derived class invokes a non-virtual method from its base, such
invocation shall not include explicit scope name to make name origin
clear, usage of explicit scope naming shall be used only when it is
necessary (multiple inheritance which should be avoided at all cost).
This also applies to non-virtual public member functions in the
interface implemented by a class.

It is required to use the “override” keyword in the derived class for
methods that are attempted to be overridden from the base class. Do not
use virtual, when override, as this is redundant information.

.. code:: cpp

   class Derived : public Base
   {
   public:
       int bar()
       {
           return foo() + 1;
       }

   private:
       int fooImpl() override
       {
           return 42;
       }
   };

.. _header-n243:

#include directives usage
^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``<>`` (brackets) when including header files into a translation
unit from C++ standard library. In all other cases, use “” (quotes).

Following order of includes is preferred. If not empty, each section
should be separated by a new line:

-  library includes - provided by compiler for example or

-  3rd party library include – boost and others

-  external project library include – CCS libraries and others

-  Internal library include – libOM_utils and others.

-  this component includes

As an exception to the rule, for source files first include shall always
be corresponding header file.

Full path to included header should always be specified, when your file
is located in the same directory as the file you are including prefer
using full path.

//source.cpp

.. code:: cpp

   #include “source.h”
   #include <memory>
   #include “boost/bind.hpp”
   #include “AaSysCom.hpp”
   #include “CFsmBase.hpp”
   #include “CellcRadParams.hpp”
   #include “CELLC_CellSetupReq.hpp”

.. _header-n262:

Forward declaration
^^^^^^^^^^^^^^^^^^^

You can use forward declaration in an attempt to save on unnecessary
compilation. This section is based on [GoogleStd].

-  Avoid forward declarations of entities defined in another project,
   including 3rd parties libraries.

-  When using a class template, prefer to include its header file.

-  Don’t change value ownership into pointer ownership just so you can
   use forward declaration.

.. _header-n271:

Undefined and unspecified behaviour
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

C++ standard [Cpp99] differentiates undefined and unspecified behaviour.
No code shall rely on either one, even if with the specific compiler
version code works correctly.

.. _header-n273:

memset vs std::fill_n
~~~~~~~~~~~~~~~~~~~~~

Always use std::fill() or std::fill\ *n() to assign a specified value to
elements of a sequence, never use memset(). std::fill() and
std::fill*\ n() shall be used to assign a specified value to elements of
a sequence of any type. Where applicable value initialization shall be
used. See also chapter 6.3.2.

memset() can only be safely applied on PODs. Data structures might
change in future to non-PODs and bear the risk of undefined behaviour:

-  Applying memset() on a class will overwrite the virtual table
   pointer.
-  Applying memset() on a class will overwrite members already
   initialized by default constructors. This double initialization at
   least slows down performance and will cause more serious problems
   when being applied e.g. on dynamic data members.

Usage of std::fill_n() is future-safe.

.. code:: cpp

   typedef int A;
   int main()
   {
       unsigned const numOfAs = 10;
       A someAs[numOfAs];

       std::fill_n(someAs, numOfAs, -1);
       return 0;
   }

Second example:

.. code:: cpp

   class A
   {
       virtual ~A()
       {
       }

       virtual void operator=(int i) = 0;
       virtual int get() = 0;
   };

   class AConcrete : public A
   {
   public:
       A() : i()
       {
       }

       void operator=(int i)
       {
           btsomLogger(LOG_DEBUG, i);
           this->i = i;
       }

       virtual int get()
       {
           return i;
       }

   private:
       int i;
   };

   int main()
   {
       unsigned const numOfAs = 10;

       A someAs[numOfAs];
       std::fill_n(someAs, numOfAs, -1);

       return 0;
   }

.. _header-n285:

Always use value initialization to set memory to zero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Always use value initialization with an empty initializer-list {} or
initialize () to set all members of a data structure to zero instead of
memset.

.. code:: cpp

   struct S
   {
       u32 u;
       bool b;
   };

   S s1 = {}; // initializes members of s1 to 0
   std::unique_ptr<S> s2(new S()); // initializes members of *s2 to 0

   class C
   {
       C()
           : i() // same as memset(i, 0, sizeof(i)), only safer!
       {
       }

   private:
       int i[10];
   };

   int* p = new int[20](); // same as int* p = new int[20];

   // memset(p, 0, 20*sizeof(int));
   // ...but safer!

Always use value initialized temporaries to reset data to zero.

.. code:: cpp

   void reset(S& s)
   {
       s = S();
   };

For value initialized data, when a data structure changes to a non-POD,
e.g. by adding a class with a default constructor, the compiler will
automatically invoke such constructors and will apply correct value
initialization for other members.

Do not use memset() to 0 instead. As outlined in the previous chapter,
any usage of memset() is only safe for PODs.

   Note that compared to memset() there is no performance penalty when
   using value initialization on PODs to initialize or reset data. If
   applicable the compiler will generate the same code and will also
   remove temporary objects.

.. _header-n294:

Never use memcpy() instead of copy constructor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Always use copy constructors and assignment operators to copy from one
object to another. Always use std::copy() to copy one sequence to
another. Never use memcpy() for any of these purposes. Usage of memcpy() is only valid for PODs. But as data types might change
over time memcpy() is not future safe. For any non-POD having a non-trivial copy constructor or assignment
operator memcpy() will result in unspecified behaviour.

The following example will result into memory leaks and double freeing
of memory:

.. code:: cpp

   class A
   {
   public:
       A()
           : i(new int())
       {
       }

   private:
       std::unique_ptr<int> i;
   };

   int main()
   {
       unsigned const numOfAs = 10;

       A a1, a2, arr1[numOfAs], arr2[numOfAs];
       memcpy(&a1, &a2, sizeof(a1)); // error!
       memcpy(arr1, arr2, sizeof(arr1)); // error!

       return 0;
   }

The memory leaks and double freeing of allocated memory get avoided by
making use of assignment operators and std::copy() algorithm in the next
example. An assignment operator for class A has to be provided, as
std::unique_ptrs assignment operator is private:

.. code:: cpp

   class A
   {
   public:
       A()
           : i(new int())
       {
       }

       A& operator=(A const& a)
       {
           *i = *a.i;
           return *this;
       }

   private:
       std::unique_ptr<int> i;
   };

   int main()
   {
       unsigned const numOfAs = 10;
       A a1, a2, arr1[numOfAs], arr2[numOfAs];
       a1 = a2;

       std::copy(arr1, arr1 + numOfAs, arr2);
       return 0;
   }

.. _header-n302:

Alternative operators
~~~~~~~~~~~~~~~~~~~~~

Using alternative operators such as not, or, and is up to developer.

.. _header-n304:

Type aliases – using, typedef
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

C++11 introduced new way of creating type aliases, which is more
readable especially for function pointers, also using alias-declaration
allows for creating template type aliases. The developer is free to use
either option.

.. code:: cpp

   using Integer = int; //standard alias for normal type
   using IntVector = std::vector<int>;

   // advantage of using - template type alias:
   template <typename T> using TemplatedVector = std::vector<T>;

.. _header-n308:

Usage of Standard, Boost and other libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following algorithm should be applied to choose a solution providing the
required functionality:

1. Is it in the Standard C++ Library? Yes: great, use it! No: go to next
   step.
2. Is it in the Boost library? Yes: great, use it! No: go to next step.
3. Is it in CC&S Library? Yes: great, use it! No: go to next step.
4. Is it in some other library we have? Yes: great, use it! No: go to
   next step.
5. Can we add a new library[1]? Yes: great, use it! No: go to next step.
6. Implement it yourself.

.. _header-n323:

Memory management
~~~~~~~~~~~~~~~~~

It is advised to use stack allocated variables over the dynamic
allocated. Use dynamic allocation when necessary, and in such cases
avoid manual memory management with explicit calls to delete operator.
Instead, std::unique_ptr or std::shared_ptr shall be used wherever
possible.

This is to ensure that code is exception safe and does not introduce
memory leaks. Also, with dynamic allocation it is hard to track objects’
lifetime.

Transferring memory ownership between different parts of code shall be
explicitly included in the interface. For such cases, use source-sink
idiom (Source/sink idiom) with smart pointers. However,
std::shared_ptr should be preferred as it simplifies testing.

.. code:: cpp

   class Untestable
   {
   public:
       Untestable(std::unique_ptr<Dependency> dep) : dep(dep)
       {}

       // other methods
   };

   class Testable
   {
   public:
       Testable(std::shared_ptr<Dependency> dep) : dep(dep)
       {}

       // other methods
   };

In the above example the first class takes ownership of the given
parameter. Therefore, passing Mock object to it is unreliable, as they
may be destroyed before checking the expectations. std::shared_ptrs can be created by constructing them from pointers
allocated using new operator or by using std::make_shared templated
function. The latter method is preferred as it is exception-safe and
improves performance of the created shared pointer [BSP45]. std::weak_ptr is a non-owning observer of an object owned by
std::shared_ptr and shall be used to avoid cyclic dependencies. Usage of std::unique_ptr should be limited to Private Implementation
Idiom [BSP45]. Usage of std::shared_array and boost::scoped_array is forbidden as
these are just C arrays with specified ownership and do not maintain its
size. Instead, use std::vector of std::unique_ptrs.

.. _header-n333:

Type casts
~~~~~~~~~~

Explicit casting shall be avoided, use proper polymorphism instead.
Where necessary, prefer using C++ style casts [Cpp99] over old C-style
[CSt99]. This ensures proper semantics in all cases and introduces
additional checks for correctness. RTTI based casts should be avoided,
depend on the polymorphism, in some cases when it is not enough there
are patterns like visitor which serve purpose of avoiding RTTI based
casting.

.. code:: cpp

   class Message
   {
   public:
       virtual ~Message()
       {
       }

       bool acceptHandler(MessageHandler& handler)
       {
           return acceptHandlerImpl(handler);
       }

   protected:
       virtual bool acceptHandlerImpl(MessageHandler& handler) = 0;
   };

   class ConcreteMessage : public Message
   {
   protected:
       bool acceptHandlerImpl(MessageHandler& handler) override
       {
           Handler.handleMessage(*this);
       }
   };

   int main()
   {
       Message* msg = receiveMessage();
       MessageHandler handler;

       // instead of handler->handleMessage(dynamic_cast<ConcreteMessage*>(msg));
       msg->acceptHandler(handler);
   }

Casting away const or volatile qualifiers must be justified, carefully
checked and documented properly. For such cases use const cast. When
necessary, conversions shall be stacked, instead of merging them in one
static or reinterpret cast.

.. code:: cpp

   const Foo* foo;
   return dynamic_cast<ConcreteFoo*>(const_cast<Foo*>(foo));

.. _header-n339:

Exceptions
~~~~~~~~~~

Exceptions shall inherit from one of the standard exceptions. For
application domain errors, use std::logic_error. Avoid using standard
exception classes directly, provide own exception class instead.

Function declaration shall not include exception specification.

When declaring public method that can throw some exception consider
naming it with a prefix of ‘try’ for example trySend, it will tell user
right away that this method can throw exception to its callers, it is in
hands of the user to check implementation to validate which exceptions
can be thrown. It is best to always throw maximum 1 kind of exception
from method.

.. _header-n343:

Containers
~~~~~~~~~~

Prefer using standard containers over plain arrays or hand coded data
structures. Default containers are std::vector for sequences, std::set
for ordered sets of unique objects and std::map for key-value
dictionaries.

Implement own container class only if profiling shows a bottleneck which
cannot be resolved using standard library. While doing so, conform to
the standard as much as possible, including, but not limited to, correct
iterators tags and typedef exported by the container. This also applies
to const versions of exposed interfaces.

Even if creating a custom container, by default use standard containers
as the internal implementation. Avoid coding complex data structures by
hand (e.g. linked lists).

.. code:: cpp

   template <typename Key, typename Data>
   class Container
   {
   public:
       typedef Data data_type;
       typedef Key key_type;
       typedef std::pair<const key_type, data_type> value_type;
       typedef unsigned long size_type;

       class iterator : public std::iterator<std::forward_iterator_tag, value_type>
       {
       public:
           typedef typename Container::value_type value_type;

           iterator();
           value_type& operator*();
           iterator& operator++();
       };

       class const_iterator : public std::iterator<std::forward_iterator_tag,
                                  const value_type>

       {
           // const iterator implementation
       };

       Container();
       iterator begin();
       const_iterator begin() const;
       iterator end();
       const_iterator end() const;
       std::pair<iterator, bool> insert(const value_type& vValue);
       iterator find(const key_type& key);
       const_iterator find(const key_type& key) const;
       size_type erase(iterator position);
       size_type erase(const key_type& key);
       void erase(iterator first, iterator last);
       void clear();
       bool empty() const;
   };

Note that iterators exposed by custom container provide standard
iterators tags, in order to enable optimization of standard algorithms
running on such a container.

.. _header-n349:

Algorithms
~~~~~~~~~~

Generally, standard algorithms should be preferred over loops, like in
listing below:

.. code:: cpp

   #include <iostream>
   #include <cctype> // for toupper
   #include <string>
   #include <algorithm>

   int main()
   {
       std::string s = " hello ";
       std::cout << "Before: " << s << std::endl; // Before: hello

       std::transform(s.begin(), s.end(), s.begin(), toupper);
       std::cout << "After: " << s << std::endl; // After: HELLO

       return 0;
   }

.. _header-n352:

Functors
~~~~~~~~

When implementing own functors for standard algorithms, one shall
conform to Adaptable Function [STL] interface. Such a functor should
export certain types as typedefs. This is to enable higher order
manipulation of such functors, particularly function composition.

The easiest way to accomplish this is to derive the functor class from
std::unary\ *function or std::binary*\ function.

.. code:: cpp

   class IsLowerCaseLetter : public std::unary_function<bool, char>
   {
   public:
     bool_type operator()(char_type char)
     {
         return (char >= ‘a’) && (char <= ‘z’);
     }
   };

.. _header-n356:

Lambdas
~~~~~~~

Lambdas were introduced in C++11 standard. They are useful in context of
standard algorithms when passing a user defined functor is needed:

.. code:: cpp

   struct Point
   {
       int x;
       int y;
   };

   std::vector<Point> V(100, Point());
   std::sort(V.begin(), V.end(), [](Point& P, Point& Q)
   {
       return P.x < Q.x;
   });

Do not use lambdas in other context. Especially, do not define lambdas
greater than 5 lines. If needed, consider creating a named functor or
function object.

Do not use default captures, write all lambda captures explicitly. For
example, instead of ``[=](int x) { return n += x; }`` use
``[n](int x) { return n+=x; }``. Before using lambda check if function
which you are trying to create does not already exists in the standard
library.

.. _header-n361:

Const usage
~~~~~~~~~~~

Use const whenever it makes sense:

-  If an argument passed by reference or pointer to a function is not
   modified, that argument should be const.

-  Class method should be const if it does not change inner state of an
   object, i.e. does not modify data members, does not call any
   non-const method and do not return a non-const pointer or non-const
   reference to a data member.

-  Class data members should be const if they are not modified after
   creation.

.. _header-n370:

Inline functions
~~~~~~~~~~~~~~~~

Adding inline keyword to the function will almost never change anything,
as it is only a hint for compiler. Inline should only be used for
template methods declared outside the class (in the same header file).
Inline keyword is applicable when defining methods in the header file
outside of the class definition.

.. _header-n372:

Explicit constructors
~~~~~~~~~~~~~~~~~~~~~

Use the C++ keyword explicit for constructors callable with one argument
to avoid undesirable auto conversions.

.. _header-n374:

Static usage
~~~~~~~~~~~~

Static keyword has different semantics depending on the place it is used
in:

-  Methods which do not access data member and do not call any
   non-static method should be static. Those methods can be treated in
   common sense as utils methods. Keep in mind that often these kinds of
   methods does not belong to this class and is often a good reason to
   try to move them somewhere else.

-  Static local variable has a scope of visibility limited to function
   it is declared, however it has a lifespan extended after function
   returns. Usage of static local should be avoided and has no place in
   the OO code.

-  Static data members have scope of a class and lifespan of global
   object. Do not use static members other than POD, because the order
   of creation of static members and global variables is undefined. So
   the order of destruction is undetermined, and destruction of one
   non-POD static variable depending on other may cause program crashes
   (e.g. in multithreaded environment).

-  Use static for global variable to limit its name scope to the cpp
   file it is defined.

.. _header-n385:

Function parameter order
~~~~~~~~~~~~~~~~~~~~~~~~

Argument order of a function is inputs and then outputs. Output
parameters are strongly discouraged.

.. _header-n387:

Ternary operator
~~~~~~~~~~~~~~~~

Using ternary operator is advisable instead of if-else one liners, only
when statement results in the same behavior. Do not use the ternary
operator as a hack around Allman.

.. code:: cpp

   int abs(int n)
   {
       return (n >= 0) ? n : -n;
   }

.. _header-n391:

Idioms and design patterns
--------------------------

.. _header-n392:

Resource Acquisition Is Initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All resources should be wrapped in a class, which allocates the resource
in its constructor, and releases it in the destructor. This ensures
proper release of the resource in case of an early return from a
function or exception being thrown from its body.

.. code:: cpp

   class File : private boost::noncopyable
   {
   public:
       explicit File(const std::string& name)
           : name(name)
       {
           fd = open(name.c_str(), O_CREAT, S_IREAD | S_IWRITE);

           if (fd <= 0)
           {
               throw std::logic_error("Could not open file ‘" + name + "’");
           }
       }

       ~File()
       {
           close(fd);
           unlink(name);
       }

   private:
       int fd;
   };

   void frobnicate()
   {
       // temporary file
       File file(" temp.txt");

       while (...)
       {
           if (logicFailed())
           {
               // thanks to RAII, file resources will be released
               throw std::runtime_excpetion(“logic failed”);
           }
       }
   }

In case of heap allocated objects, one should use smart pointer to
handle memory. This is especially useful in Factory Methods utilizing
Builder pattern [GHJV95], i.e. when one needs to do non-trivial
initialization of a heap-allocated object outside its constructor.

.. code:: cpp

   std::unique_ptr<Object> createObject()
   {
       std::unique_ptr<Object> object(new Object());
       // if one of these fails, memory is released

       object->initializeFirst();
       object->initializeSecond();

       return std::move(object);
   }

.. _header-n398:

Interfaces
~~~~~~~~~~

For most of cases plain interface with all virtual non-static method and
without members or implementation is preferred. Virtual destructor with
empty inline implementation is advised for such interfaces, do not
declare the virtual destructors as pure virtual = 0, as it forces users
to provide their own implementation of destructors even when it will be
empty.

.. code:: cpp

   class Value
   {
   public:
       virtual ~Value()
       {}

       virtual void calculate() = 0;
   };

Interfaces shall appear at the top of class hierarchy, it is not
recommended inherit one interface from another. Multiple inheritance is
allowed only from interfaces and, as an exception, CRTP and policy
classes.

Note that once member function is made virtual in the base class, it
stays virtual in the whole hierarchy. Therefore, one shall add override
keyword to respective member functions in all derived classes, in order
to emphasize function’s origin and to rely on compiler in case of any
typos.

Pay extra attention to make derived classes satisfy Liskov substitution
principle ([LW99], section 5). In cases where such a relationship is not
clear and/or hard to explain, prefer aggregation over inheritance and
forward selected calls to the aggregated object.

.. _header-n404:

CRTP
~~~~

Curiously Recurring Template Pattern (CRTP) is a construct where a class
inherits from template instantiated with the class as a parameter, as
follows:

.. code:: cpp

   template <typename T>
   class ThisIsCrtp
   {
       // ...
   };

   class User : public ThisIsCrtp<User>
   {
       // ...
   };

This idiom uses inheritance in a non-orthodox way, in order to inject
some code into the derived class. Such cases are not considered
interfaces and interface naming rules do not apply. That being said, it
is strongly encouraged to find a meaningful name, instead of just adding
a generic “Base” suffix.

Multiple inheritance from CRTP templates is allowed, but using them as a
“normal” base class to e.g. take an argument to a function is forbidden.

.. _header-n409:

Source/sink
~~~~~~~~~~~

Transferring memory ownership is a common case in message-based
architectures. Such semantics is directly supported in the C++ language
itself by means of std::unique_ptr template class.

In order to use the idiom, one needs to explicitly declare which class
allocates memory (or some other resource) and which one releases it.
This has to be decided upfront and should not be changed.

.. code:: cpp

   class MessageReceiver
   {
   public:
       std::unique_ptr<Message> receiveMessage()
       {
           std::unique_ptr<Message> msg;

           // do some logic to fill in msg

           msg = new Message(...);
           return msg;
       }
   };

   class MessageHandler
   {
   public:
       // note passing auto pointer by value and no explicit release

       void handleMessage(std::unique_ptr<Message> msg)
       {
           // do some logic to interpret message contents
       }
   };

Such implementation ensures that ownership of the message is transferred
safely and there are no memory leaks, i.e. when exception is thrown by
MessageHandler logic.

.. _header-n414:

Policy classes and type traits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Policy and trait classes are used in generic and generative programming
[Ale01] as a way to achieve static polymorphism of a template code. Such
class shall have a Policy or Traits suffix, depending on the actual
functionality.

Trait classes are class templates parameterized by a single type,
containing a set of constants and operations connected and describing a
type, regardless where the type is used. Using such a class in a generic
code instead of hard-coded calls enables greater flexibility and allows
user to adapt the code easily. Such classes usually have all members
public, so it is advised to declare them with a struct.

Note that in the following example RAII idiom is also used for exception
safety.

.. code:: cpp

   template <typename LockType>
   struct LockTraits;

   template <typename T, typename LockType = pthread_mutex_t>
   class Safe
   {
   public:
       void put(const T& value)
       {
           typename LockTraits<LockType>::ScopeLock lock(lock);
           value = value;
       }

       T get()
       {
           typename LockTraits<LockType>::ScopeLock lock(lock);
           value = value;
       }

   private:
       LockType lock;
       T value;
   };

   template <>
   struct LockTraits<Mutex>
   {
       class ScopeLock : private boost::noncopyable
       {
       public:
           ScopeLock(Mutex& mutex)
               : mutex(mutex)
           {
               pthread_mutex_lock(&mutex);
           }

           ~ScopeLock()
           {
               pthread_mutex_unlock(&lock.mutex);
           }

       private:
           Mutex& mutex;
       };
   };

   template <>
   struct LockTraits<Semaphore>
   {
       class ScopeLock : private boost::noncopyable
       {
       public:
           ScopeLock(Semaphore& sem)
               : sem(sem)
           {
               sem_wait(&sem);
           }

           ~ScopeLock()
           {
               sem_post(&sem);
           }

       private:
           Semaphore& sem;
       };
   };

Policy classes, on the other hand, allow modification of generic code
that uses them, as a well-defined extension points. This effectively
implements compile-time Strategy design pattern [GHJV95]. Note that
great attention must be paid while defining policies, especially when
generic code uses multiple policies, as they should be orthogonal and
the code should support all possible combinations. If this is not
possible and some policy sets are mutually exclusive, one should use
static assertion to stop the compilation with a meaningful message.

For details, refer to [Ale01], as the topic is too complicated to
include it in a coding standard document.

.. _header-n422:

Private Implementation (pImpl)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dependencies between different parts of the code shall be kept minimal.
This applies particularly to extensive use of templates and generic
code, when including a lot of header files can lead to very long
compilation times.

One way to limit internal dependencies is to hide class implementation
in so-called private implementation class. This ensures that only public
interface of the class is exposed, and all private members are
completely unknown to the user, but requires the developer to ensure
proper construction and copying of the internal object.

Note that while this idiom significantly improves encapsulation, it has
some impact on performance and introduces large maintenance overhead.
Therefore it shall only be used in case of stable classes that are
unlikely to change during refactoring.

One should also pay extra attention to proper copying of the data. For
clarity, this issue is avoided in the example by making the class
non-copyable.

.. code:: cpp

   #pragma once

   #include <memory>
   #include “boost / utility.hpp”
   #include “Message.hpp”

   namespace coding
   {
   class QueueImpl;

   class Queue : private boost::noncopyable
   {
   public:
       typedef std::shared_ptr<Element> ElementPtr;

       Queue();
       Queue(const Queue& rhs);
       ElementPtr pop();
       void push(ElementPtr element);

   private:
       std::unique_ptr<QueueImpl> impl;
   };

.. code:: cpp

   #include “Queue.h”
   #include <queue>
   #include “Mutex.hpp”

   namespace coding
   {
   // hide implementation details in cpp file

   class QueueImpl
   {
   public:
       Queue::ElementPtr pop()
       {
           Queue::ElementPtr element = queue.front();
           queue.pop();

           return element;
       }

       void push(Queue::ElementPtr element)
       {
           queue.push(element);
       }

   private:
       std::queue<ElementPtr> queue;
   };

   // ensure proper construction

   Queue::Queue()
       : impl(new QueueImpl)
   {
   }

   Queue::Queue(const Queue& rhs)
       : impl(new QueueImpl(* rhs.impl))
   {
   }

   // forward call to internal implementation

   Queue::ElementPtr Queue::pop()
   {
       return impl->pop();
   }

   void Queue::push(ElementPtr element)
   {
       impl->push(element);
   }
   }

.. _header-n430:

Filesystem, system interactions – Dependency Injection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When working with file system or system commands, it’s best to use
dedicated classes. Please study the following example, where production
class MessageHandler has to read file contents and then execute a system
command. Thanks to the dedicated classes like BtsOmCommand and
FileAccess we can freely stub the behavior of system in our unit tests.
Note that BtsOmCommand and FileAccess classes are just examples.

.. code:: cpp

   #pragma once
   #include “BtsOmCommand.h”
   #include “FileAccess.h”

   class MessageHandler
   {
   public:
       MessageHandler(std::unique_ptr<BtsOmCommand> command,
                      std::unique_ptr<FileAccess> fileAccess)
         : command(command), fileAccess(fileAccess)

      {
      }

      void execute()
      {
          std::string fileContents = fileAccess->readContent(“file.txt”);
          if (fileContents == “Valid”)
          {
              command->move(“file.txt”, “valid.txt”);
          }
          else
          {
              command->removeForce(“file.txt”);
              throw std::logic_error(“Unexpected file contents”);
          }
      }
   };

.. _header-n433:

Smart pointers, pointers and references – when to use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use smart pointers to inform users about pointer ownership. Type of
pointer should carry important information to the user. A raw pointer
should tell that the pointer will be deleted somewhere else, unique
pointer should tell user that he is to take care of memory cleanup, and
lastly, shared pointer tells that you want to participate in keeping the
object alive.

For function parameters, in most cases you should still use raw pointers
or, preferably, references. Use raw pointer over references only when
you want to handle nullptr case. Prefer raw pointers and references in
parameters over smart pointers unless you want to take care of the
ownership of the object. It’s okay to use .get() or dereference the
smart pointer instead of polluting the interfaces with smart pointers.

Guideline on way of passing the function parameters:

-  by value: function uses copy of argument

-  by reference: function does not participate in ownership (cannot
   handle nullptr)

-  by pointer: function does not participate in ownership (can handle
   nullptr)

-  by unique pointer: function gets ownership of this object

-  by shared pointer: function wants to take part in ownership and can
   store it for further use

When returning pointers from functions use similar guidelines: return
smart pointers to indicate memory ownership and raw pointers just to
give the client access to particular object without transferring
ownership. For example, factory methods usually should return
unique_ptrs, but situation may differ depending on the use case. Watch
[CCon14] and read [CppCore] for details.

.. _header-n449:

Refactoring
-----------

This chapter contains information to help you decide when to consider
refactoring. It lists some known code smells. For the sake of good
practice, the list below should also be considered when writing new
code.

1. Method / function length – shorter functions are preferred to larger ones (empty lines or curly braces are not counted):

   1. 0-10: perfect
   2. 10-20: should be considered for refactoring
   3. 20+: poor, shall be considered for refactoring

2. Duplicate code:

   1. more than 40% of one method is copied to another method
   2. obvious cases of duplicate code across methods and classes
   3. use the Sonar and CPD (Copy/Paste Detector) tools on Jenkins to easily check code duplication

3. Parameter list length:

   1. 0-2: perfect
   2. 3-4: acceptable
   3. 5+: consider split function into few or (less preferred) the use of structures or classes as parameter types, or builder pattern

4. Wrong usage of comments:

   1. if comments are obvious, remove them
   2. if algorithm is complicated, describe it explicitly; it is up to the developer to either provide text or a DOORS reference
   3. method implementation requires too many comments
   4. change comment to named object: function, variable or constant


5. Conditional complexity (number of conditions as part of a conditional statement) – low complexity functions are preferred:

   1. 0-2 conditions: perfect
   2. 3-4 conditions: acceptable
   3. 5-6 conditions: time to consider writing a new method for this condition
   4. 7+ conditions: list of arguments is too long

6. Large classes – “god Objects”:

   1. classes that hold multiple responsibilities

7. Inappropriate Intimacy:

   1. class uses implementation details of another class (except UTs)

8. Poorly named methods or members:

   1. name does not follow lowerCamelCase
   2. name uses not well known or unnecessary abbreviations (please write
      config instead of cnfg)
   3. name is too long (see chapter 2.6 for details)
   4. type is embedded in the name
   5. inconsistent method names (e.g. if a function open() is defined, then its opposite should be named close())

9. Dead code:

   1. remove commented out code

10. Too many primitive type members:

    1. try to find out if some members are closely related and encapsulate
       them into a separate class / structure

11. Broken Liskov substitution principle:

    1. overridden methods break contact with the inherited class, therefore objects of the derived class cannot be used in place of objects of
       the inherited class; to fix this, consider aggregation instead of
       inheritance

12. Nested conditions:

    1. 0-1: Perfrect
    2. 2: acceptable
    3. 3+: move most nested conditions to new function

.. _header-n584:

Testing - UT
------------

For existing component all new unit tests should be designed and written
using GTest/GMock framework. During development of new component some
other framework could be used, if there is a good enough reason to do
so.

.. _header-n586:

Strategy
~~~~~~~~

The main testing strategy to be used in OAM is black box testing. This
means that one should focus on testing public interface of a
class/service. No macros #define protected public are allowed.

Although not recommended, it might be necessary to extend the test case
with white box testing in order to achieve sufficient code coverage. One
shall do that by modifying code under test to expose members as
protected and implement a testable version of the original class.
Exposed members can only be accessed using getters returning by value
and setters:

.. code:: cpp

   namespace cellp
   {
   class CellManagement
   {
       // note the full scope to avoid ambiguity

   protected:
       int state;
       // application code follows
   };
   }

   // test code

   namespace cellp
   {

   class TestableCellManagement : public CellManagement
   {
       int getState() const
       {
           return state;
       }

       void setState(int newState)
       {
           state = newState;
       }
   };
   }

Aside from such declarations it is forbidden to pollute application code
with sections related to unit tests.

.. _header-n591:

Structure
~~~~~~~~~

Each class should have its own unit test. It is recommended to put unit
tests for each class in a separate compilation unit. However if two or
more classes provide similar functionality it is allowed to provide one
test set for all of them.

.. code:: cpp

   class MessageReceiverTestSuite : testing::Test
   {
   public:
       MessageReceiverTestSuite(); // optional constructor
       ~MessageReceiverTestSuite(); // optional destructor

       void SetUp() override; // optional setup
       void TearDown() override; // optional teardown
       void helper(); // optional helper methods
   };

   TEST_F(MessageReceiverTestSuite, shouldFailWhenGivenUnexpectedEvent)
   {
       // testing code
   }

Each test should be registered using TEST\ *F macro provided by Google
Test, TEST macro if no fixture is required or TEST*\ P for parameterized
tests.

.. _header-n595:

Pre-conditions and post-conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common initialization code, including preconditions, method shall be
implemented within the test constructor or SetUp() method. TearDown()
method or destructor, on the other hand, shall release all resources
allocated in either SetUp() or test case itself. It is strongly
recommended to perform all actions which are required to leave the
environment in a state as it was before test case, this may include
clearing singleton instances.

It is forbidden to reuse other test cases as preconditions. If few test
has the same preconditions it should be provided by some function. If
one test can be run only, when other was executed before one can merge
this testecases into one test.

Note that it might be necessary to enable white box testing in a
particular piece of code to simplify unit test. This is especially valid
for state machines, where access to private members allows the test to
set desired state directly, without going through declared flow.
Enabling white box testing is assumed better than reusing test cases as
preconditions.

.. _header-n599:

Logging test execution
~~~~~~~~~~~~~~~~~~~~~~

While GTest provides basic functionality to generate test execution log,
one might need to put additional debug logs, especially if the test case
is non-trivial. Such logs shall be generated using the same
stream–oriented API as in application logs. There is possibility to run
tests with printing logs.. It would be best however that the tests be
simple enough to localise the problem without such logs.

.. _header-n601:

Unit tests vs. System Component Tests (SCT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The differences between SCTs and UTs are defined in order to avoid
overlapping, which would increase required maintenance. The main
difference is the fact that SCTs run on the whole, unmodified, system
component, while unit tests are executed on the parts of code, with rest
simulated with mocks.

Also, SCT cases shall have direct mapping to use cases described in
functional specification documents. Unit tests, on the other hand, shall
not interact with the real platform (CC&S), as they can be isolated
using proper stubs. Unit tests shall neither send nor receive any
messages from SC’s external interface.

UT code shuld be treated as production code, means all described rules
and good practices apply to them unless explicity stated otherwise.

.. _header-n605:

Refactoring
~~~~~~~~~~~

One of the goals of unit testing is to protect the developer during
refactoring. Therefore unit tests should never be disabled while
refactoring production code.

A simple example of an approach of class and unit test extraction:

1. Introduce a factory for the original class in the production code,

2. Verify that integration tests (SCTs) pass,

3. Extract the methods and members into a new class and replace the
   relevant code with uses of the extracted class methods (do not modify
   the tests!),

4. Verify that unit tests pass,

5. Use Dependency Injection to inject the extracted class into the
   original,

6. Verify that the whole regression passes,

7. Cover the extracted class with characterization tests,

8. Replace the extracted class with a Mock Object in the original tests
   (do not modify the production code),

9. Verify that unit tests pass.

.. _header-n627:

Naming convention
~~~~~~~~~~~~~~~~~

.. _header-n628:

Unit Test Files – Tests
^^^^^^^^^^^^^^^^^^^^^^^

Unit test filenames shall correspond to the name of file being tested,
with additional Test suffix, e.g. MessageSenderTest.cpp. Unit test shall
consist of the implementation file only, as headers for test suites are
not needed.

As to location follow convention in the project.

.. _header-n631:

Unit Test Files – Test Doubles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unit test doubles [Doubles] for a specific part of the code shall be
stored in the Doubles directory UT/Doubles/Include and UT/Doubles/Source
directory, mimicking directory structure of production code. That is,
mock for class Include/namespace/Class.h should have its Mock located in
UT/Doubles/Include/namespace/ClassMock.h. There shouldn’t be separate
directories for different Test Doubles, as in Stubs Dummies etc, each
should go into the same directory as class being Doubled.

All test doubles should be inside appropriate Doubles directory relative
to the original class that is being mocked e.g.:

.. code::

   SC_OAM/OM_PIL/Include/BS.h
   SC_OAM/OM_PIL/UT/Doubles/Include/BsMock.h

Nested directories example:

.. code::

   SC_OAM/OM_PIL/Include/enbc/types/Nested.h
   SC_OAM/OM_PIL/UT/Doubles/Include/enbc/types/NestedMock.h

.. _header-n637:

Test suites
~~~~~~~~~~~

All test suites shall mimic the namespaces where original class are
located.

.. code:: cpp

   // production ../Include/locking/Functionality

   namespace locking
   {
   class Functionality
   {
   };

   }

   // UT/Include/locking/Functionality

   #include “locking/Functionality.h”
   #include “gtest/gtest.h”

   namespace locking
   {

   class FunctionalityTest : public ::testing::Test
   {
   };

   }

..

   Listing 50. Namespace usage in test suites

.. _header-n642:

Test cases
~~~~~~~~~~

The name should be a sentence describing the results of the entity under
test. The subject can be omitted if it is implicit.

Examples:

.. code:: cpp

   TEST_F(InitialContextSetupHandlerTest, releasesUeIfPayloadIsNotValid)
   TEST_F(InitialContextSetupHandlerTest, shouldReleaseUeIfPayloadIsNotValid)
   TEST_F(InitialContextSetupHandlerTest, testIfUeIsReleasedWhenPayloadIsNotValid)
   TEST(UeContainerTest, findShouldReturnNullPtrWhenUeIdIsNotFound)

In case of doubt about test case names, you can use following notation:
`testedMethod\_ <>`__\ [whenYYY\_]shouldZZZ (note that the [] means
optional).

.. code:: cpp

   TEST_F(EnbcTest, release_givenValidPayload_whenEnbcIsNotReady_shouldQueueTheMessage)
   TEST_F(EnbcTest, whenEnbcIsNotReady_shouldQueueTheMessage)
   TEST_F(EnbcTest, release_givenInvalidPayload_shouldThrow)

Test cases should follow the AAA (Arrange Act Assert) layout shown
below:

.. code:: cpp

   TEST_F(OamTest, release_givenValidPayload_whenEnbcIsNotReady_shouldQueueTheMessage)
   {
       // arrange (given) – prepare environment for specific test case
       // act (when) – execute actions taking you to state you want to test
       // assert (should) – assertions, check result
   }

This may not be applicable to legacy or characterization tests.
Descriptive names should be as self–explanatory as possible. In
particular they shall not include DOORS references (e.g. CP 1234), as
these numbers are subject to change.

If the goal of two or more methods is to test given functionality in two
different ways (e.g. with different control flow), further naming
extension might be necessary. Like with all names, apply good taste and
common sense.

.. _header-n652:

Comments
~~~~~~~~

Each test case can be commented using standard doxygen format if
necessary. Such a description should contain pre– and post–conditions
for the test case and a general explanation of the test scenario.

.. _header-n654:

Helper code
~~~~~~~~~~~

Helper functions used in unit tests should be declared as member
functions of the test suite class. If a helper class is needed, it is
advised to define it as private nested classes of the test suite or a
class in an anonymous namespace:

.. code:: cpp

   struct MessageReceiverTestSuite : testing::Test
   {
       // helper class generating messages:
       class MessageFactory
       {
           // ...
       };

   protected:
      void testMessageDispatch();

   private:
      // helper function generating messages:

      template <typename Message>
      Message* createMessage();
   };

In case of helper classes that are used by multiple test suites, it’s
allowed to define them in separate files (and/or namespaces).

.. _header-n658:

Google mock compilation speed-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When mocking big classes with many member functions (e.g.
MockConfigMgrService), it is advised to add empty implementation of
mock’s constructor and destructor in separate source file to speed up
compilation. The source file should be added to
../UT/Doubles/Source/MockConfigMgrService.cpp

Detailed explanation: for every mocked member function, also a
non-trivial template based data member is added. When compiler generates
the default constructor and destructor it has to instantiate constructor
for all such data members. By moving the constructor and destructor
implementation to source file, this code will be compiled only once
instead of every time the mocked class is instantiated in given
translation unit.

.. _header-n661:

Terms and Abbreviations
-----------------------

   IDE Integrated Development Environment, application integrating text
   editor, build system, code navigation etc., e.g. Eclipse or Visual
   Studio

   POD Plain Old Data, type that has concrete binary representation and
   can be copied in binary mode (i.e. old C structures)

   STL Standard Template Library, C++ library providing containers and
   algorithms general use, predecessor of C++98 Standard Library

   CRTP Curiously Recurring Template Pattern

   OAM Operation and Maintenance

   CC&S Common Computer & Support Software

.. _header-n669:

References
----------

   [Ale01] Andrei Alexandrescu. Modern C++ Design: generic programming
   and design patterns applied. Addison-Wesley, 2001.

   [Cpp99] ISO-IEC 14882:2003, C++ Programming Language. International
   Standards Organization, 1999.

   [CSt99] ISO-IEC 9899:1999, C Programming Language. International
   Standards Organization, 1999.

   [GHJV95] Erich Gamma, Richard Helm, Ralph Johnson, and John
   Vlissides. Design Patterns. Addison-Wesley, 1995.

   [LW99] Barbara Liskov and Jeanette Wing. Behavioural sub typing using
   invariants and constraints. 1999.

   [MS98] Leonid Mikhajlov and Emil Sekerinski. A study of the fragile
   base class problem. 1998.

   [SA04] Herb Sutter and Andrei Alexandrescu. C++ Coding Standards: 101
   Rules, Guidelines, and Best Practices (C++ in Depth Series).
   Addison-Wesley, 2004.

   [STL] Standard template library reference manual.

   [Sut00] Herb Sutter. Exceptional C++: 47 engineering puzzles,
   programming problems, and solutions. Addison-Wesley, 2000.

[CppLTE]
https://sharenet-ims.inside.nokiasiemensnetworks.com/Guest/Open/D528156880

   [CCon14] Herb Sutter. Back to the Basics! Essentials of Modern C++
   Style. CppCon 2014. https://youtube.com/watch?v=xnqTKD8uD64 (12:10 –
   28:22)

   [CppCore] Bjarne Stroustrup, Herb Sutter. C++ Core Guidelines. 2015.

   https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#f42-return-a-t-to-indicate-a-position-only

   [GoogleStd] Google Coding Standard.
   `https://google.github.io/styleguide/cppguide.html <https://google.github.io/styleguide/cppguide.html%20>`__

   [Doubles] https://en.wikipedia.org/wiki/Test_double

   [Formatter]
   https://workspaces-emea.int.nokia.com/sites/FZFT12KRK/Wiki/Review
   process.asp
