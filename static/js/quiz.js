angular.module('quiz', [])
	.controller('mainController', ['$scope','$http', function($scope,$http) {
		$scope.init = function(qid){
			$scope.quiz_id=qid;
			$scope.getQuestion();
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
		$scope.setLifeline = function(type){
			$scope.llType = type;
			if(type==1)
				$scope.llDesc = 'This will skip this question. You will not get points for this level.';
			else if(type==2)
				$scope.llDesc = 'This will give you hint. 5 points will be reduced from current score.';
			else
				$scope.llDesc = 'This will give you link of page. 5 points will be from current score.';
		}
		$scope.useLifeline = function(){
			$scope.loading = true;
			$http.post('/quiz/'+$scope.quiz_id+'/uselifeline',{"level":$scope.que.level,"type":$scope.llType})
				.success(function(data){
					if(data.status=="success")
					{
						showSB('Lifeline Unlocked.','success');
						if(data.type==1)
						{
							$scope.getQuestion();
						}
						else if(data.type==2)
						{
							$scope.llHint = data.hint;
						}
						else if(data.type==3)
						{
							$scope.llLink = data.link;
						}
						$scope.lbUpdate();
					}
					else if(data.status=="fail")
					{
						showSB('Already Used.','warning');
					}
					else
					{
						showSB('Error : Contact Coordinatior.','danger');
					}
					$scope.loading = false;
				});
		}
		$scope.getQuestion = function(){
			$scope.loading = true;
			$http.post('/quiz/'+$scope.quiz_id+'/getquestion')
				.success(function(data){
					$scope.que = data;
					$scope.llHint="";
					$scope.llLink="";
					$scope.lbUpdate();
					$scope.loading = false;
				});
		}
		$scope.checkAnswer = function(){
			$scope.loading = true;
			$http.post('/quiz/'+$scope.quiz_id+'/checkanswer',{"level":$scope.que.level,"answer":$scope.answer})
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
						showSB('Error : Contact Coordinatior.','danger');
					}
					$scope.loading = false;
				});
		}
		$scope.lbUpdate = function(){
			$scope.loading = true;
			$http.post('/quiz/'+$scope.quiz_id+'/gettop')
				.success(function(data){
					$scope.lbData = data;
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