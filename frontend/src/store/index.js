import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items: [],
    switch_check: false,
    count: 0,
    user_id: ''
  },
  getters: {
    getItems(state) {
      console.log(state.items)
      return state.items
    },
    getState(state){
      return state.switch_check
    },
    getCount(state){
      return state.count
    },
  },
  mutations: {
    updateItems(state, data) {
      state.items = data
    },
    setState(state, switcher){
      state.switch_check = switcher
    },
    setCount(state, num){
      state.count = num
    },
  },
  actions: {
    loadItems({commit}) {
      axios.get('http://127.0.0.1:8000/users')
      .then(res => {
        commit('updateItems', res.data)
      })
    },
    setState(context, value) {
      context.commit('setState', value);
    },
    setCount(context, num){ 
      context.commit('setCount', num);
    },
  }
})