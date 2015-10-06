
Sous Chefs
-------------
**newslynx-sc-homepage** provides access to the following Sous Chefs

Time on Homepage
~~~~~~~~~~~~~~~~

-  Checks your homepage for content items and computes how long each
   article has been promoted over time.
-  This Sous Chef runs the python module
   ``newslynx_sc_homepage.metrics.TimeOnHomepage``.
-  API Slug: ``homepage-to-content-timeseries``

Usage
^^^^^

Standalone
''''''''''

Run this Sous Chef via the api, passing in arbitrary runtime options,
and stream it's output.

.. code:: shell

    $ newslynx api sous-chefs cook -d=newslynx_sc_homepage/homepage_to_content_timeseries.yaml --passthrough **options

Run this Sous Chef via the api, and if applicable, send it's output to
bulkload.

.. code:: shell

    $ newslynx api sous-chefs cook -d=newslynx_sc_homepage/homepage_to_content_timeseries.yaml **options

Do either of the above two, but pass in a recipe file

.. code:: shell

    $ newslynx api sous-chefs cook -d=recipe.yaml

Recipes
'''''''

Add this Sous Chef to your authenticated org

.. code:: shell

    $ newslynx api sous-chefs create -d=newslynx_sc_homepage/homepage_to_content_timeseries.yaml

Create a Recipe with this Sous Chef with command line options.

.. code:: shell

    $ newslynx api recipes create sous_chef=homepage-to-content-timeseries **options

Alternatively pass in a recipe file.

.. code:: shell

    $ newslynx api recipes create sous_chef=homepage-to-content-timeseries --data=recipe.yaml

Save the outputted ``id`` of this recipe, and execute it via the API.
**NOTE** This will place the recipe in a task queue.

.. code:: shell

    $ newslynx api recipes cook id=<id>

Alternatively, run the Recipe, passing in arbitrary runtime options, and
stream it's output: **NOTE** Will not execute the SousChef's ``load``
method.

.. code:: shell

    $ newslynx api recipes cook id=<id> --passthrough **options

Development
'''''''''''

Pass runtime options to ``homepage-to-content-timeseries`` and stream
output. **NOTE** Will not execute the SousChef's ``load`` method.

.. code:: shell

    $ newslynx sc-run newslynx_sc_homepage/homepage_to_content_timeseries.yaml option=value1

Alternatively pass in a recipe file

.. code:: shell

    $ newslynx sc-run newslynx_sc_homepage/homepage_to_content_timeseries.yaml --recipe=recipe.yaml

Options
^^^^^^^

In addition to default recipe options,
``homepage-to-content-timeseries`` also accepts the following

-  ``page``

   -  The url of the homepage to monitor

   -  **Required**
   -  Should be rendered with a ``text`` form.
   -  Accepts inputs of type:

      -  ``url``

Metrics
^^^^^^^

``homepage-to-content-timeseries`` generates the following Metrics

-  ``time_on_homepage``

   -  Display name: ``Time on Homepage``

   -  Type: ``count``

   -  Content Levels:

      -  ``timeseries``
      -  ``summary``
      -  ``comparison``

   -  Org Levels:

      -  ``timeseries``
      -  ``summary``



