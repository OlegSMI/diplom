import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items: [],
    switch_check: false,
    count: 0,
    user_id: '',
    notes: ''
  },
  getters: {
    getItems(state) {
      return state.items
    },
    getState(state){
      return state.switch_check
    },
    getCount(state){
      return state.count
    },
    getTodoById: (state) => (id) => {
      return state.items.find(item => item.id === id)
    },
    getNotes(state){
      return state.notes
    }
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
    setNote(state, note){
      state.notes = note
    }
  },
  actions: {
    loadItems({commit}) {
      axios.get('http://127.0.0.1:8000/all_users')
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
    setNote(context, note){
      context.commit('setCount', note);
    }
  }
})