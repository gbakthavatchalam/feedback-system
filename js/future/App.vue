<template>
  <div id="app">
   <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
            <h5 class="my-0 mr-md-auto font-weight-normal"><router-link to = "/">Home</router-link>
            <nav class="my-2 my-md-0 mr-md-3">
                <router-link to = "/list">View All</router-link>
            </nav>  
        </div>
    <div class="container">
	<router-view/>
    </div>
  </div>
 </template>
