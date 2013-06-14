# Backbone-tastypie-mixin

This is a slightly modified version of Paul Uithol's Backbone-tastypie that
leaves the standard Backbone.sync, Model and Collection prototypes alone and
instead adds a TastypieMixin.ModelMixin object and
TastypieMixin.CollectionMixin object that can be mixed in to your models and
collections explicitly. Especially useful when using multiple external APIs,
all of which are not Tastypie-backed.

A small conversion layer to make [backbone.js](https://github.com/documentcloud/backbone) work together happily with
[django-tastypie](https://github.com/toastdriven/django-tastypie). Other REST APIs conforming to the same style are
also compatible. See for example [TastyMongo](https://github.com/ProgressiveCompany/TastyMongo).

Backbone-tastypie-mixin is available under the [MIT license](https://github.com/azundo/backbone-tastypie-mixin/blob/master/LICENSE.txt).

Backbone-tastypie depends on [Backbone](https://github.com/documentcloud/backbone) (1.0.0 or newer),
and thus on [Underscore](https://github.com/documentcloud/underscore) (1.4.4 or newer).

## Contents

* [Installation](#installation)
* [How it works](#how-it-works)
* [Settings](#settings)
* [Methods](#methods)

## Installation

Add `backbone_tastypie_mixin` to your `INSTALLED_APPS` setting, and add the following to your base template:

```html
<script type="text/javascript" src="{{ STATIC_URL }}js/underscore.js"></script>
<script type="text/javascript" src="{{ STATIC_URL }}js/backbone.js"></script>
<script type="text/javascript" src="{{ STATIC_URL }}js/backbone-tastypie-mixin.js"></script>
```

Mix in where neccessary.
```javascript
var MyTastypieModel = Backbone.Model.extend(Backbone.TastypieMixin.ModelMixin).extend({
    prop1: val1,
    ...
});

var MyTastypieCollection = Backbone.Collection.extend(Backbone.TastypieMixin.CollectionMixin).extend({
    prop1: val1,
    ...
});
```

## How it works

Backbone-tastypie-mixin provides a several Backbone mixins for compatibility
with django-tastypie. These mainly have to do with `Backbone.sync`, building
urls for models and collections, and parsing data.

## Settings

Backbone-tastypie-mixin supports several global API settings in the `Backbone.Tastypie` namespace.

##### doGetOnEmptyPostResponse

Default: `true`

By default, Tastypie doesn't return data after a `POST`. Enabling this setting performs an extra `GET` request to fetch
new data for the newly created model from the server. If you have control over the server, you can also enable the
[always-return-data](http://django-tastypie.readthedocs.org/en/latest/resources.html#always-return-data)
option on your (Model)Resources.

##### doGetOnEmptyPutResponse

Default: `false`

By default, Tastypie doesn't return data after a `PUT`. Enabling this setting performs an extra `GET` request to fetch
new data for the updated model from the server. If you have control over the server, you can also enable the
[always-return-data](http://django-tastypie.readthedocs.org/en/latest/resources.html#always-return-data)
option on your (Model)Resources.

##### apiKey

An object containing a `username` and a `key`.

##### csrfToken

Set the current csrf token. See https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax. You can also load the
value from a cookie like this (provided you have the jQuery.cookie plugin installed):

```javascript
Backbone.Tastypie.csrfToken = $.cookie( 'csrftoken' );
```

## Methods

##### Backbone.TastypieMixin.sync

`TastypieMixin.sync` performs an additional `GET` request if there is no response body after creating an object
(see `doGetOnEmptyPostResponse`), or after updating an object (see `doGetOnEmptyPutResponse`).

##### Backbone.TastypieMixin.ModelMixin.url

##### Backbone.TastypieMixin.ModelMixin.parse

##### Backbone.TastypieMixin.CollectionMixin.parse

##### Backbone.TastypieMixin.CollectionMixin.url

`Backbone.TastypieMixin.CollectionMixin.url` can build urls for a set of models. This is for example useful
when using the `fetchRelated` method in [Backbone-relational](https://github.com/PaulUithol/Backbone-relational/).
