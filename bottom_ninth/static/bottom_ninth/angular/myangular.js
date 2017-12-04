console.log('testing');

const app = angular.module('MyApp', ['ngRoute']);

app.controller('MainController', [function(){
	this.test = 'test';
}])