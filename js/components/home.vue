<template>
	  <div class="row">
	    <div class="col-md-8 order-md-1">
	      <h4 class="mb-3">Your Feedback</h4>
	      <form class="needs-validation" novalidate="">
		<div class="row">
		  <div class="col-md-6 mb-3">
		    <label for="firstName">First name</label>
		    <input v-model="firstName" type="text" class="form-control" id="firstName" placeholder="" required="">
		    <div class="invalid-feedback">
		      Valid first name is required.
		    </div>
		  </div>
		  <div class="col-md-6 mb-3">
		    <label for="lastName">Last name</label>
		    <input v-model="lastName" type="text" class="form-control" id="lastName" placeholder="" required="">
		    <div class="invalid-feedback">
		      Valid last name is required.
		    </div>
		  </div>
		</div>
		<div class="mb-3">
		  <label for="email">Email</label>
		  <input v-model="emailId" type="email" class="form-control" id="email" placeholder="you@example.com" required="">
		  <div class="invalid-feedback">
		    Please enter a valid email address.
		  </div>
		</div>
		<div class="mb-3">
		  <label for="message">Message</label>
		  <textarea v-model="message" class="form-control" id="message" required=""></textarea>
		  <div class="invalid-feedback">
		    Please provide your feedback.
		  </div>
		</div>


		<hr class="mb-4">
		<button v-on:click="onSubmit" class="btn btn-primary btn-lg btn-block">Submit</button>
	      </form>
	    </div>
	  </div>
</template>


<script>
export default {
  name: 'home',
  data () {
    return {
      firstName: "",
      lastName: "",
      emailId: "",
      message: "",
    }
  },
  methods:{
	onSubmit: function(){
                        alert(this.message);
        }
  }
}
</script>
