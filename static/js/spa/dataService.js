
questApp.factory('menu', function($http){
	return {
		list: function(callback){
			$http.get('/api/mark/').success(callback);
		}
	};
});

questApp.factory('markFactory', function($http) {
 return{
    getPhotos : function() {
        return $http({
            url: '/api/mark/',
            method: 'GET'
        })
    }
 }
});



questApp.factory('Data', function ($http, $q) {
    return {
        ajaxItems: function () {
            var deferred = $q.defer();
            $http({ method: "GET", url: "/api/mark/?format=json" })
                .success(function (data, status, headers, config) {
                    deferred.resolve(data);
                }).error(function (data, status, headers, config) {
                    deferred.reject(status);
                });
            return deferred.promise;
        }
    }
});
