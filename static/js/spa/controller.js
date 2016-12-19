/**
 * Created by cyber on 13.12.16.
 */


questApp.controller('MainController', function ($scope, $activityIndicator, $timeout) {
    var myElement = document.querySelector("#back");
    myElement.style.display = "none";
        var elem = document.querySelector("#printer");
    elem.style.display = "none";
    $activityIndicator.startAnimating();
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);
});
questApp.factory('advesting', function ($http) {
    return {
        list: function () {
            $http.get('/api/mark/');
        }
    };

});

questApp.controller('NewAutoController', function ($scope, $http, $activityIndicator, $timeout) {
    var myElement = document.querySelector("#back");
    myElement.style.display = "block";
        var elem = document.querySelector("#printer");
    elem.style.display = "none";
    $activityIndicator.startAnimating();
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);
    $http.get('/api/mark/?format=json')
        .then(function (response) {
            $scope.marks = response.data;
        });

});
questApp.controller('TOController', function ($scope, $activityIndicator, $timeout) {
    var myElement = document.querySelector("#back");
    elem.style.display = "block";
        var elem = document.querySelector("#printer");
    elem.style.display = "none";
    $activityIndicator.startAnimating();
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);

});
questApp.controller('MarkController', function ($scope, $http, $activityIndicator, $timeout) {
    var myElement = document.querySelector("#back");
    myElement.style.display = "block";
    var elem = document.querySelector("#printer");
    elem.style.display = "none";
    $activityIndicator.startAnimating();
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);
    $http.get('/api/mark/?format=json')
        .then(function (response) {
            $scope.marks = response.data;
        });
});
questApp.controller('MarkModelController', function ($scope, $http, GetShop, $routeParams, $activityIndicator, $timeout) {
    var myElement = document.querySelector("#back");
    myElement.style.display = "block";
    var elem = document.querySelector("#printer");
    elem.style.display = "none";

    $activityIndicator.startAnimating();
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);
    $scope.currentId = $routeParams.id;
    $http.get('/api/autos/' + $scope.currentId + '?format=json')
        .then(function (response) {
            $scope.marks = response.data;
            console.log($scope.marks);
        });

});

questApp.controller('ModelController', function ($scope, $http, GetShop, $routeParams, $activityIndicator, $timeout) {
    var myElement = document.querySelector("#back");
    myElement.style.display = "block";
    var myElement = document.querySelector("#printer");
    myElement.style.display = "block";
    $activityIndicator.startAnimating();
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);
    $scope.currentId = $routeParams.id;
    $scope.color = "";
    $http.get('/api/auto/' + $scope.currentId + '?format=json')
        .then(function (response) {
            $scope.model = response.data;
            if (response.data.color == "красный") {
                $scope.color = "red";
            }
            if (response.data.color == "черный") {
                $scope.color = "black";
            }
            if (response.data.color == "синий") {
                $scope.color = "blue";
            }
            if (response.data.color == "серый") {
                $scope.color = "grey";
            }
            if (response.data.color == "белый") {
                $scope.color = "white";
            }
            if (response.data.color == "коричневый") {
                $scope.color = "brown";
            }
            if (response.data.color == "голубой") {
                $scope.color = "blue";
            }
        });


    $scope.carousel = function (currentTarget) {
        var id_selector = $(currentTarget).attr("id");
        var id = id_selector.substr(id_selector.length - 1);
        id = parseInt(id);
        $('#myCarousel').carousel(id);
        console.log(id);
        setTimeout(function () {
            $('[id^=carousel-selector-]').children('img').removeClass('ad');
            $(currentTarget).children('img').addClass('ad');
        }, 700);
    };

    $('#myCarousel').bind('slide.bs.carousel', function (e) {
        setTimeout(function () {
            var id = $('.active').data('slide-number');
            id = parseInt(id);
            $('[id^=carousel-selector-]').children('img').removeClass('ad');
            $('[id^=carousel-selector-' + id + ']').children('img').addClass("ad");
        }, 700);


    });
    $scope.prev = function () {
        $('#myCarousel').carousel('prev');
    };
    $scope.next = function () {
        $('#myCarousel').carousel('next');
    };
    $scope.th_prev = function () {
        $('#Carousel').carousel('prev');
    };
    $scope.th_next = function () {
        $('#Carousel').carousel('next');
    };

    $scope.coll = function (currentTarget) {
        $('.panel').toggleClass('collapse-open');
        $('.panel').toggleClass('collapse-close');
        $('.panel-title').toggleClass('collapsed-o')
    };


});

questApp.factory('GetShop', function ($http) {
    return function (id) {
        return $http({
            method: 'GET',
            url: '/api/autos/' + id + '/',
        });
    }
});
questApp.controller('SellerController', function ($document, $scope, $http, $activityIndicator, $timeout) {
    $activityIndicator.startAnimating();
        var elem = document.querySelector("#printer");
    elem.style.display = "none";
    $timeout(function () {
        $activityIndicator.stopAnimating();
        console.log("asd");
    }, 1000);
    $http.get('/api/seller/?format=json')
        .then(function (response) {
            $scope.citys = response.data;
        });
    var myElement = document.querySelector("#back");
    myElement.style.display = "block";
});

