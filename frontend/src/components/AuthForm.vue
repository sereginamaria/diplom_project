<template>
    <div class="w-100 h-100 position-absolute d-flex flex-column justify-content-center align-items-center">
        <form class="row g-3"
              @submit.prevent="loginUser"
        >
            <div class="col-12">
                <label for="inputLogin" class="form-label">Логин</label>
                <input class="form-control" id="inputLogin"
                       placeholder="Введите логин"
                       v-model="login"
                >
            </div>
            <div class="col-12">
                <label for="inputPassword" class="form-label">Пароль</label>
                <input type="password" class="form-control" id="inputPassword"
                       placeholder="Введите пароль"
                       v-model="password"
                >
            </div>
            <div class="col-12 d-flex justify-content-center">
                <MyButton style="width: 250px" class="blue-buttons">Войти</MyButton>
            </div>
        </form>

        <div style="color: lightgrey; position: absolute; bottom: 0; right: 0">v-0.0.0.</div>

    </div>

    <MyModal v-model:show="modalVisible" v-model:buttons="modalButtons"
             @update="checkAnswer"
    >
        {{this.modalMessage}}
    </MyModal>
</template>

<script>
    import axios from "axios";

    export default {
        name: "AuthForm",
        data() {
            return {
                login: '',
                password: '',
                modalVisible: false,
                modalButtons: [],
                modalMessage: ''
            }
        },
        methods: {
            loginUser(){
                axios.get("http://localhost:8090/auth", {
                    login: this.login,
                    password: this.password
                })
                    .then(function (response) {
                        console.log(response)
                    })
                    .catch(function () {
                    })
                axios.get("http://localhost:8070/users", {
                    login: this.login,
                    password: this.password
                })
                    .then(function (response) {
                        console.log(response)
                    })
                    .catch(function () {
                    })
            },
            checkAnswer(){
                this.modalVisible = false
            }
        },
        mounted(){
            console.log('auth')
        }
    }
</script>

<style scoped>
</style>