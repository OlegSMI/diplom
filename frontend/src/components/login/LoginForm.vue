<template>
   <v-app>
      <v-main>
         <v-container fluid fill-height>
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                 <v-alert type="error" v-if="this.erroralert==true">
                  Неверный логин или пароль, повторите попытку.{{vision}}
                </v-alert>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="primary">
                        <v-toolbar-title>Вход в аккаунт</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                     <form ref="form" @submit.prevent="login()">
                            <v-text-field
                              ref="username"
                              v-model="username"
                              :rules="[() => !!username || 'This field is required']"
                              prepend-icon="mdi-account"
                              label="Логин"
                              placeholder="TotallyNotThanos"
                              required
                           />
                            <v-text-field
                              ref="password"
                              v-model="password"
                              :rules="[() => !!password || 'This field is required']"
                              :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                              :type="showPassword ? 'text' : 'password'"
                              prepend-icon="mdi-lock"
                              label="Пароль"
                              placeholder="*********"
                              counter
                              required
                              @keydown.enter="login"
                              @click:append="showPassword = !showPassword"
                            />
                           <div class="red--text"> {{errorMessage}}</div>
                           <v-btn class="mt-4" color="primary" value="log in" @click="regUser">{{stateObj.login.name}}</v-btn>
                      </form>
                     </v-card-text>
                  </v-card>
                
               </v-flex>
            </v-layout>
         </v-container>
      </v-main>
   </v-app>
</template>

<script>
export default {
  name: "App",
  props: {
    vision:
    {
      type:Boolean,
      }
   },
  data() {
    return {
      username: "",
      password: "",
      isRegister : false,
      errorMessage: "",
      showPassword:false,
      erroralert: false,
      stateObj: {
         login : {
            name: 'Войти',
         }
      }
    };
  },
  methods: {
    login() {
      const { username } = this;
      this.$router.replace({ name: "dashboard", params: { username: username } });
    },
  regUser(){
    if (this.username == "admin" && this.password == "admin") {
      this.$emit('updateVision', true)
      this.$router.push('Home') 
    }
    else { 
      this.erroralert=true;
      }
    
  },
  },
      computed: {
      
    }
};
</script>