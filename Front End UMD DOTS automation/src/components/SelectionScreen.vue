<script setup>
//there will always be something in writing that says what updates/changes have occured, just a matter of finding where it is coming from
import {useRoute,useRouter} from 'vue-router'
import { onBeforeMount, onMounted, ref } from 'vue'
const route = useRoute()
const router = useRouter()

const items = ref([{ message: 'Administrative'},{ message: 'All Campus'},{ message: 'Alumni'},{ message: 'Any Campus Meter'},{ message: 'Breaksgiving'},{ message: 'Bus Bundle Pack'},{ message: 'Campus Meter'},{ message: 'Construction'},{ message: 'Courier'},{ message: 'EMBA'},{ message: 'Emeritus'},{ message: 'LPR Emeritus'},{ message: 'FS Bundle Packs'},{ message: 'Faculty/Staff'},{ message: 'FAE (UMUC)'},{ message: '(2022-2023) UMGC Permits'},{ message: '(2023-2024) UMGC Permits'},{ message: '(2024-2025) UMGC Permits'},{ message: '(2024-2025) FS Green Permits'},{ message: 'Gate Cards'},{ message: 'Golden ID Commuter'},{ message: 'Lot 1 Commuter'},{ message: 'Lot 10 Courtyards'},{ message: 'Lot 8 Courtyards'},{ message: 'Lot 11 Commuter'},{ message: 'Lot 15 Resident'},{ message: 'Lot 16 Resident'},{ message: 'Lot 19 Resident'},{ message: 'Lot 2 Resident'},{ message: 'Lot 3 Commuter'},{ message: 'Lot 3 Resident'},{ message: 'Lot 4 Commuter'},{ message: 'Lot 6 Commuter'},{ message: 'Lot 6 Resident'},{ message: 'Lot 9 Commuter'},{ message: 'Medical Permit'},{ message: '(23-24, 23-25, 24-26) Micromobility'},{ message: 'Motorcycle (No Permit)'},{ message: 'Lot 11 Overnight Storage'},{ message: 'Lot 16 Overnight Storage'},{ message: 'Lot 17 Overnight Storage'},{ message: 'Lot 19 Overnight Storage'},{ message: 'PUNCH OUT- ONE HOUR'},{ message: 'Quarantine/Isolation'},{ message: '24-25 Scooter'},{ message: 'Service Permit (Paper)'},{ message: 'Service'},{ message: 'Short Term Parking'},{ message: 'Lot SDG Commuter'},{ message: 'Student Bundle Pack'},{ message: 'Student Daily Permits'},{ message: 'Student Lot B'},{ message: 'Student Lot U2'},{ message: 'Student Lot UU'},{ message: 'Student Lot XX'},{ message: 'Summer Commuter'},{ message: 'Summer Resident'},{ message: 'Surface Lot'},{ message: 'Temporary Faculty/Staff'},{ message: 'Temporary Lot Assignment'},{ message: 'Time and Materials'},{ message: 'Temporary Permit'}])
const count = ref(0)
const unrestrictedPast4 = ["9b","10a","11b","Lot 1b","Lot 1c", "Lot 1d", "Lot 1f", "4a", "4b", "4h","4j","4k","4m","4n","4t","6","A", "B", "C1", "CC1", "CC2", "FF2", "J1","J2","JJ3", "K5", "K7","N","NN","O5","P1","P2","PH1","Q","RR","RR2","S9","UU","U2","V2","V3","X1","XX1","YY","Z"]
const permitToParkingMap = new Map();
const nightPermit = new Set(["Lot 11 Overnight Storage", "Lot 16 Overnight Storage","Lot 17 Overnight Storage","Lot 19 Overnight Storage","Lot SDG Overnight Storage"])
permitToParkingMap.set("Lot 11 Overnight Storage", new Set(["Lot 11b"]))
permitToParkingMap.set("Lot 16 Overnight Storage", new Set(["Lot 16a","Lot 16b", "Lot 16f"]))
permitToParkingMap.set("Lot 17 Overnight Storage", new Set(["Lot 17a"]))
permitToParkingMap.set("Lot 19 Overnight Storage", new Set(["Lot 19"]))
permitToParkingMap.set("Lot SDG Overnight Storage", new Set(["SDG"]))
permitToParkingMap.set("Lot 1 Commuter", new Set(["Lot 1b","Lot 1c", "Lot 1d", "Lot 1f"]))
permitToParkingMap.set("Lot 4 Commuter", new Set(["4a", "4b", "4h","4j","4k","4m","4n","4t"]))
permitToParkingMap.set("Lot 3 Commuter", new Set(["3"]))
permitToParkingMap.set("Lot 9 Commuter", new Set(["9b"]))
permitToParkingMap.set("Lot 6 Commuter", new Set(["6"]))
permitToParkingMap.set("Lot 11 Commuter", new Set(["Lot 11b"]))
permitToParkingMap.set("Lot 16 Resident", new Set(["Lot 16a","Lot 16b", "Lot 16f"]))
permitToParkingMap.set("Lot 19 Resident", new Set(["Lot 19"]))
permitToParkingMap.set("Lot 2 Resident", new Set(["2"]))
permitToParkingMap.set("Lot 6 Resident", new Set(["6"]))
permitToParkingMap.set("Summer Commuter", new Set(["9b","SDG","Lot 19","Lot 17a","Lot 16a","Lot 16b", "Lot 16f","Lot 11b","Lot 1b","Lot 1c", "Lot 1d", "Lot 1f","6"]))
permitToParkingMap.set("Summer Resident", new Set(["9b","SDG","Lot 19","Lot 17a","Lot 16a","Lot 16b", "Lot 16f","Lot 11b","Lot 1b","Lot 1c", "Lot 1d", "Lot 1f","6"]))
permitToParkingMap.set("Faculty/Staff", new Set(["K3","UU","U1","U2","V2","V3","X1","XX1","Z","SDG","Lot 1b","Lot 1c", "Lot 1d", "Lot 1f", "4a", "4b", "4h","4j","4k","4m","4n","4t","6","8","9b","10a","11b","12a","14a","14b","14c","15","16a","16b","16f","17a","19"]))

const backendAPI = "http://localhost:3000/"

function removeAllInstances(array, elementToRemove) {
  let i = 0;
  while (i < array.length) {
    if (array[i] === elementToRemove) {
      array.splice(i, 1);
    } else {
      i++;
    }
  }
  return array
}



async function sumbit(){
  let personal = []
  for(let i =1; i<=3; i++){
    if(document.getElementById("auth"+i).checked){
      personal.push(document.getElementById("lab"+i).innerHTML);
    }
  }
  if(personal.length!=1){
    alert("Looks like there's a logical error in your input. Make sure you're only selecting one personal type")
    return;
  }

  let permits = []
  for(let i=0; i<items.value.length; i++){
    if(document.getElementById(items.value[i].message).checked){
      permits.push(items.value[i].message)
    }
  }
  document.getElementById("sumbit").style.backgroundColor = "white"
  document.getElementById("sumbit").style.color = "black"
  document.getElementById("sumbit").innerHTML = "PROCESSING, PLEASE BE PATIENT. MAY TAKE A MINUTE..."

  let lots = getLots(permits,personal[0]);
}

async function getLots(permits,personal){
  const router = new useRouter()
  let PossibleLots = []

  const time = new Date();  
  console.log(time.getHours())
  if(time.getHours()>=16 || (time.getHours()>=0 && time.getHours()<3) || time.getDay()==0 || time.getDay()==6){
    PossibleLots=PossibleLots.concat(unrestrictedPast4);
  }

  if(personal.localeCompare("Student")){
    if(time.getHours()>=3 && time.getHours()<5){
      for(let i = 0; i<permits.length; i++){
        if(nightPermit.has(permits[i])){
          PossibleLots = PossibleLots.concat(Array.from(permitToParkingMap.get(permits[i])))
        }
      }
    }else{
      for(let i = 0; i<permits.length; i++){
        PossibleLots = PossibleLots.concat(Array.from(permitToParkingMap.get(permits[i])))
      }
    }

  }else if(personal.localeCompare("Faculty")){
    if(time.getHours()>=3 && time.getHours()<5){
      
    }else{
      PossibleLots = PossibleLots.concat(Array.from(permitToParkingMap.get("Faculty/Staff")))
    }
  }

  let text = document.getElementById("prompt").value
  if(text.trim().localeCompare("") != 0){

    
    let prmpt1 = text+"\n\nBased on the given information above, what lots can we park in given the current date-time is "+time+" and that we are a "+personal+"?" +
                        "The list of all availble lots on the University of Maryland, College Park campus: K3,UU,U1,U2,V2,V3,X1,XX1,Z,SDG,Lot 1b,Lot 1c, Lot 1d, Lot 1f,"+
                        " 4a, 4b, 4h,4j,4k,4m,4n,4t,6,8,9b,10a,11b,12a,14a,14b,14c,15,16a,16b,16f,17a,19,2,AA,A,B,BB,C1,CC1,CC2,CY,D,"+
                        "DD,E,F,FF2,G,GG1,GG2,HC,HH,HP,J1,J2,JJ1,JJ3,K3,K5,K7,KK,L,LL1,LL2,LL3,LL4,LL6,LL5,MM1,MM2,MM3,N,N3,N4,N6,N7,"+
                        "N8,N9,NN,O1,O3,O5,P1,P2,PH1,PH2,PH2,Q,Q1,QQ,R2,R3,R4,RR,RR2,S3,S7,S8,S9,SS1,SS2,T,TT,TV,U1,UU,U2,V2,V3,W,W1,Y,YC,YY.\\n\\n"+
                        "Give an output that is a strictly just a list of comma delinated lots. \nfor example: \nLot 1b,4a,4b"
    const prmptResponse1 =  await fetch(backendAPI, {
          method: "POST",
          body: prmpt1
      });
    let addedLotsText = await prmptResponse1.text()
    const addedLots = addedLotsText.split(",");
    for(let i = 0; i<addedLots.length; i++){
      addedLots[i] = addedLots[i].trim()
    }
    PossibleLots = PossibleLots.concat(addedLots);


    let prmpt2 = text+"\n\nBased on the given information above, what lots are restricted, and are no longer availbe to park in given the date-time is "+time+" and that we are a "+personal+"? "+
                        "The list of all availble lots on the University of Maryland, College Park campus: K3,UU,U1,U2,V2,V3,X1,XX1,Z,SDG,Lot 1b,Lot 1c, Lot 1d, Lot 1f,"+
                        " 4a, 4b, 4h,4j,4k,4m,4n,4t,6,8,9b,10a,11b,12a,14a,14b,14c,15,16a,16b,16f,17a,19,2,AA,A,B,BB,C1,CC1,CC2,CY,D,"+
                        "DD,E,F,FF2,G,GG1,GG2,HC,HH,HP,J1,J2,JJ1,JJ3,K3,K5,K7,KK,L,LL1,LL2,LL3,LL4,LL6,LL5,MM1,MM2,MM3,N,N3,N4,N6,N7,"+
                        "N8,N9,NN,O1,O3,O5,P1,P2,PH1,PH2,PH2,Q,Q1,QQ,R2,R3,R4,RR,RR2,S3,S7,S8,S9,SS1,SS2,T,TT,TV,U1,UU,U2,V2,V3,W,W1,Y,YC,YY.\\n\\n"+
                        "Give an output that is a strictly just a list of comma delinated lots. \nfor example: \nLot 1b,4a,4b"
    const prmptResponse2 =  await fetch(backendAPI, {
          method: "POST",
          body: prmpt2
    });
    let removableLotsText = await prmptResponse2.text()
    const removableLots = removableLotsText.split(",");
    for(let i = 0; i<removableLots.length; i++){
      removableLots[i] = removableLots[i].trim()
    }
    for(let i = 0; i<removableLots.length; i++){
      let k = 0
      while (k < PossibleLots.length) {
        if (PossibleLots[k] == (removableLots[i])) {
          PossibleLots.splice(k, 1);
        } else {
          k++;
        }
      }
    }
  }

  let arr = [...new Set(PossibleLots)];
  const Lots = Array.from(arr)
  let lotStr = ""
  for(let i = 0; i<Lots.length-1; i++){
    lotStr+=Lots[i]+", ";
  }
  lotStr+=Lots[Lots.length-1];
  makeup(lotStr)
}

function makeup(fr){


  console.log(fr)
  router.push({ path: '/result/'+fr  })
}

</script>

<template>
  <div id="title">
    <div id="mapTogle">MAP
      <img id="map" src="https://transportation.umd.edu/sites/default/files/inline-images/2024_Campus%20Maps_Website-01_0.jpg">
    </div>
    <div id="ex">UMD Parking</div>
  </div>
<div id="block">
  <div id="questions">
    <div id="q">
      Are you a faculuty, student, or visitor?
    </div>
    <div id="selecs">
      <div id="opt">
        <input type="checkbox" class="auth" id="auth1">
        <label for="auth1" id="lab1"> Visitor</label>
      </div>
      <div id="opt">
        <input type="checkbox" class="auth" id="auth2">
        <label for="auth2" id="lab2"> Student</label>
      </div>
      <div id="opt" >
        <input class="auth" type="checkbox" id="auth3">
        <label for="auth3" id="lab3"> Faculty</label>
      </div>
    </div>
    
    <div id="q">
      Are registered for any permits on campus? (Map Toggle for refrence above)
      <div id="note">
        note: only put non expired permits. If you have a permit from a previous semester that has expired, please do not list it here
      </div>
    </div>
    <div id="selecs">
      <li  id="opt2" v-for="item in items">
          <input class="auth" type="checkbox" :id="item.message">
          <label> {{ item.message }}</label>
      </li>
    </div>
  </div>
  <div id="q">
      Are there more nuanced permisions you've been given? Explain bellow in written english.
  </div>
  <textarea id="prompt">

  </textarea>
  <div @click="sumbit" id="sumbit">
      FIND VALID LOTS
  </div>


</div>




</template>

<style scoped>
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
  position: fixed;
  top: 443px;
  left: 50%;
  transform: translate(-50%, -50%);  
  display:none;
  width:800px;
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
  background-color: rgb(50, 50, 50);
  border-color:black
}
.auth{
  background-color: rgb(0, 203, 203);
}
</style>
