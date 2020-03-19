.. _use_case_template:

Use case template (``use_case_template``)
=========================================

.. csv-table::
    :widths: 7, 40

    "Feature Ref.:", "Related feature list"
    "Req Ref.:", "Link to referenced requirement (SE level)"
    "HW unit:", "Units list that this requirement will be applicable for, i.e. FZM, FZC, AirScale"
    "Actors:", "Internal and external components that will participate in use case, i.e. RROM, FaReco"

**Purpose:**
------------

Short description why this requirement is needed, what functionality it covers etc.

Plain text

**Preconditions:**
------------------

Conditions under which described use case is valid and can occur.

#. First condition
#. Second condition

**Triggers:**
-------------

Conditions that fulfilling them starts execution of use case.

#. First Trigger
#. Second Trigger

**Description:**
----------------

Step by step, what happens in use case, messages sent, side effects, what actions should be performed.
Should correspond with next section.

#. First Step
    - sub step or explanation
#. Second Step

**Diagrams:**
-------------

Any diagrams that can put requirement in more convenient form to read (flow charts, communication scheme etc.)

.. uml::

    @startuml
    Title
        Title of use case
    End title

    box "Local plane" #LightBlue
        participant "Component 1"
        participant "Component 2"
    end box

    box "External plane 1" #LightGreen
        participant "External Component 1"
    endbox

    box "External plane 2" #LightYellow
        participant "External Component 2"
    endbox

    autonumber "<font color=red>[0]"
    "External Component 1" -> "Component 1" : Message 1
    "Component 1" -> "Component 2" : Message 2
    "Component 2" -> "External Component 2" : Message 3

    @enduml

**Postconditions:**
-------------------

State in which system is left after execution of use case steps.

#. First postcondition
    - sub condition or explanataion
#. Second postcondition

**Exceptions:**
---------------

Any exceptions that may occur should be noted here.

[Step # : Exception #] exception description

#. Action to be taken
    - sub action
    - sub action
#. Another action to be taken

**References:**
---------------

Links to anything mentioned in description. Includes referenced sub-usecases, mappings, external specifications, etc.

**Notes and Issues:**
---------------------

Anything is worth mentioning that can help in understanding use case. Any form is allowed.

This use case was prepared using standard use case template: :ref:`use_case_template` (Do not remove)