Vue.component('nav-bar', {
	template:`
	<div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
	    <h5 class="my-0 mr-md-auto font-weight-normal"><a href="/">Feedback Collection</a></h5>
            <nav class="my-2 my-md-0 mr-md-3">
		<a href="/list">View All</a>
	    </nav>
	</div>
	`

})

Vue.component('review', {
	props: ['name', 'emailid', 'message'],
	template: `
	    <div class="card" style="width: 50rem;">
		<div class="card-body">
                    <h6 class="card-subtitle mb-2 text-muted">{{ name }}  ({{ emailid }}) </h6>
       	            <p class="card-text"> {{ message }} </p>
	        </div>
	    </div>
	`
})




var app= new Vue({
	el: '#app',
	data: {
		currentRoute: window.location.pathname,
		firstName: "",
		lastName: "",
		emailId: "",
		message: "",
		reviewList: [],
		showSuccess: false
	},
	methods: {
		validateForm(){
			if (!(this.firstName && this.lastName && this.emailId && this.message)){
				return false;
			}
			else{
				return true;
			}
		},
		onSubmit(){
			if (this.validateForm()) {
				axios.post('/api/feedback', {
    					firstname: this.firstName,
					lastname: this.lastName,
					emailid: this.emailId,
					message: this.message
  				  })
				  .then(response => {
					this.showSuccess = true;
				  })
				  .catch(function (error) {
					    console.log(error);
			  	});
			}
		},
		getList(){
		 	axios.get('/api/feedback')
			.then(response => {
				this.reviewList = this.reviewList.concat(response.data);
			});
  		}

	},
	computed: {
		renderComponent: function(){
			return this.reviewList.length > 0;
		}
	},
	created: function(){
		if(window.location.pathname == "/list"){
			this.getList();
                }
	}
});

