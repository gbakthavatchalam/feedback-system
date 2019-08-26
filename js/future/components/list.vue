<template>
	<div v-if=len(reviewList)>
                    <review 
                        v-for="item in reviewList"
                        v-bind:key="item.id"
                        v-bind:name="item.name"
                        v-bind:emailid="item.emailid"
                        v-bind:message="item.message">
                    </review>
        </div>
</template>

<script>
	export default{
		name:'list',
		data(){
			return{
				reviewList: []
			}
		},
		methods: {
			getList: function(){
                        axios.get('/api/feedback')
                                  .then(function (response) {
                                    // handle success
                                    this.reviewList(response)
                                    console.log(response);
                                  })
                                  .catch(function (error) {
                                    this.reviewList = []
                                    console.log(error);
                                  })
                                  .finally(function () {
                                    // always executed
                                  });
                	}
		}
	}
</script>
