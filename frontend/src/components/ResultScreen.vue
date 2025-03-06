<script setup>

//there will always be something in writing that says what updates/changes have occured, just a matter of finding where it is coming from

import { ref } from 'vue'
import {useRoute,useRouter} from 'vue-router'

const route = useRoute()
const router = useRouter()

const time = new Date();

const props = defineProps({
  Lots: String,
})


function back(){
  router.push("/")
}

</script>

<template>
  
  <div id="title">
    <div @click="back" id="mapTogle">BACK
    </div>
    <div id="ex">UMD Parking</div>
  </div>
  <div id="block">
    <div id="descrip">
      <div style="margin-top:60px; width:600px; margin:auto;">As of now at {{time}}, You are able to park in the following lots:</div>
      <div style="padding-top:60px; width:600px; margin:auto;">{{ route.params.lots }}</div>
    </div>
    <img id="map" src="https://transportation.umd.edu/sites/default/files/inline-images/2024_Campus%20Maps_Website-01_0.jpg">
  </div>
  




</template>

<style scoped>
#descrip{
  color:black;
  z-index: 10;
  width:800px;
  height:250px;
  background-color: aliceblue;
}
textarea{
  color:black;
  max-width:790px;
  min-width:790px;
  max-height:100px;
  min-height:100px;
  background-color: white;

}
#sumbit{
  display:block;
  margin:auto;
  padding:35px;
  background-color:rgb(98, 2, 2);
}
#note{
  font-size:10px;
  position:relative;
  top:7px;
  width:500px; 
  display:block;
  margin:auto;
}
#ex{
  display:inline-block;
  margin:auto;
  font-size:50px;
}
#mapTogle:hover {
  background-color: rgb(118, 11, 3);
  font-size: 18px;
}
#mapTogle:hover  #map{
  display:block;
}
#mapTogle{
  display:inline-block;
  padding:10px;
  width:35px;
  background-color: rgb(169, 0, 0);
  position: relative;
  left:-200px;
  top:-10px;
}
#map{
  position: relative;
  margin:auto;
  display:block;
  width:500px;
}
input[type="checkbox"]:checked+label:before {
    background: #0021b3;
    text-align: center;
}
#opt2{
  color:black;
  display:inline-block;
  margin-right:10px;
  width:200px;
  height:100px;
  position:inherit ;
  margin-left:0;
}
#opt{
  color:black;
  display:inline-block;
  margin-left:50px;
}
#selecs{
  background:white;
  height:auto;
  padding:30px;
}
#q{
  display:block;
  margin:auto;
  padding:30px;
  background-color:black;
}
#p{
  font-size:100px;
}
#title{
  display:block;
  margin:auto;  
  background-color: black;
  padding-top: 50px;
  padding-bottom: 50px;

}
#block{
  display:block;
  margin:auto;
  overflow:auto;
  width:800px;
  height: 70vh;
  background-color: aliceblue;
  border-color:black
}
.auth{
  background-color: rgb(0, 203, 203);
}
</style>
