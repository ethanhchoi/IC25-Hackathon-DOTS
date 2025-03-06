import {createWebHistory, createRouter} from 'vue-router'
import SelectionScreen from  "../components/SelectionScreen.vue"
import ResultScreen from "../components/ResultScreen.vue"



const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
      {
        path:"/",
        component: SelectionScreen
      },
      {
        path:"/result/:lots",
        component: ResultScreen
      }
    ]
  })


  

export default router