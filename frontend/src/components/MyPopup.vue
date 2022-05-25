<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn text class="grey ma-3" dark v-on="on">Проверить парсинг</v-btn>
      </template>
      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>Add a New Project</v-card-title>
        <v-card-text>
            <v-form class="px-3" ref="form">
                <v-text-field label="Title" v-model="title" prepend-icon="mdi-folder" :rules="inputRules"></v-text-field>
                <v-textarea label="Information" v-model="content" prepend-icon="mdi-lead-pencil"></v-textarea>
                <v-menu v-model="menu">
                    <template v-slot:activator="{ on }">
                        <v-text-field :value="formattedDate" label="Due date" prepend-icon="mdi-calendar-range" v-on="on"></v-text-field>
                    </template>
                    <v-date-picker v-model="due"></v-date-picker>
                </v-menu>
                <v-spacer></v-spacer>
                <v-btn text class="success mx-0 mt-3" @click="submit">Add project</v-btn>
            </v-form>
        </v-card-text>
      </v-card>

    </v-dialog>
  </div>
</template>

<script>
import format from 'date-fns/format'
import parseISO from 'date-fns/parseISO'
export default {
    data() {
        return {
            title: '',
            content: '',
            due: null,
            inputRules: [
                v => v.length >= 3 || 'Fuck, overwrite, pidor'
            ]
        }
        
    },
    methods: {
        submit() {
            if(this.$refs.form.validate()){
                console.log(this.title, this.content)
            }

        }
    },
    computed: {
        formattedDate() {
            return this.due ? format(parseISO(this.due), 'do MMM yyyy') : ''
        }
    }
}
</script>