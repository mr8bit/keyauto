var questApp = angular.module('questApp', ["ngRoute", "ngAnimate","ngActivityIndicator"])
    .config(function ($routeProvider) {
        $routeProvider.when('/',
            {
                templateUrl: '/static/js/spa/views/main.html',
                controller: 'MainController'
            });
        $routeProvider.when('/auto',
            {
                templateUrl: '/static/js/spa/views/auto.html',
                controller: 'NewAutoController'
            });
        $routeProvider.when('/auto/mark/',
            {
                templateUrl: '/static/js/spa/views/mark.html',
                controller: 'MarkController'
            });
        $routeProvider.when("/auto/mark/:id/", {
            templateUrl: '/static/js/spa/views/mark_model.html',
            controller: "MarkModelController",
        });
         $routeProvider.when("/auto/:id/", {
            templateUrl: '/static/js/spa/views/model.html',
            controller: "ModelController",
        });
        $routeProvider.when('/technical_inspection',
            {
                templateUrl: '/static/js/spa/views/technical_inspection.html',
                controller: 'MarkController'
            });
        $routeProvider.when('/seller',
            {
                templateUrl: '/static/js/spa/views/seller.html',
                controller: 'MarkController'
            });
     });
