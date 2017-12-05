console.log('testing');

const app = angular.module('MyApp', ['ngRoute']);

app.config(['$locationProvider', function($locationProvider){
	$locationProvider.html5Mode({ enabled: true });
}]);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
	$routeProvider
		.when('/', {
			templateUrl: '',
			controller: 'MainController'
		})
		.otherwise({
			redirectTo: '/'
		});
}]);

app.controller('MainController', [function(){
	this.test = 'test';
}])