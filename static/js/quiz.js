angular.module('quiz', [])
	.controller('mainController', ['$scope','$http', function($scope,$http) {
		function getsbc(){
			return 
		}
		var options =  {
			content: 'initial',
			style: "snackbar",
			timeout: 2000 ,
			htmlAllowed: true 
		}
		function showSB(text,type){
			options.content='<div class="panel panel-'+type+'"><div class="panel-heading"><h3 class="panel-title">'+text+'</h3></div></div>'
			$.snackbar(options);
		}
		$scope.getQuestion = function(){
			$scope.loading = true;
			$http.post('/quiz/getquestion')
				.success(function(data){
					$scope.que = data;
					$scope.loading = false;
				});
		}
		$scope.checkAnswer = function(){
			$scope.loading = true;
			$http.post('/quiz/checkanswer',{level:$scope.que.level,answer:$scope.answer})
				.success(function(data){
					if(data.status=="true")
					{
						$scope.answer="";
						showSB('GoodJob','success');
						$scope.getQuestion();
					}
					else if(data.status=="false")
					{
						showSB('Wrong Answer. Try Again.','warning');
					}
					else
					{
						showSB('Cehcking...','info');
					}
					$scope.loading = false;
				});
		}
	}]).run(run)
	.config(function($interpolateProvider) {
		$interpolateProvider.startSymbol('{$');
		$interpolateProvider.endSymbol('$}');
	});;
	
	run.$inject = ['$http'];
  
	function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	};