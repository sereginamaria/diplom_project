<template>
    <div class="container-fluid d-flex justify-content-between nav-bar">
        <div>
            <MyButton data-bs-toggle="collapse" data-bs-target="#collapse-instruction" aria-expanded="false"
                      aria-controls="collapse-instruction" style="background: transparent; border-color: white">
                Показать инструкцию <span><img src="../assets/fill.svg" style="margin: auto 0 auto 5px"></span>
            </MyButton>
            <div id="collapse-instruction" class="collapse">
                <div class="card card-body">
                    <div>
                        <p v-if="mainJSON.task1Show">{{mainJSON.task1.instruction}}</p>
                        <p v-if="mainJSON.task2Show">{{mainJSON.task2.instruction}}</p>
                        <p v-if="mainJSON.task3Show">{{mainJSON.task3.instruction}}</p>
                    </div>
                    <div class="d-flex justify-content-end">
                        <p style="font-style: italic; width: 700px; text-align: right;">
                            Все имена и события в тесте вымышлены, любые совпадения с реальными людьми и событиями случайны.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="d-flex align-items-center text-center">
            <div class="d-flex flex-column" style="width: 200px">
                <p style="color: white;">Осталось времени:</p>
                <p style="color: white;">
                    {{this.mainJSON.ret}}
                </p>
            </div>
            <MyButton style="background: #F3AE4E; border-color: #F3AE4E" class="ml-3" @click="exit">Выйти</MyButton>
        </div>
    </div>

    <MyModal v-model:show="modalVisible" v-model:buttons="modalButtons"
             @update="checkAnswer"
    >
        {{this.modalMessage}}
    </MyModal>
</template>

<script>
    import {mapGetters, mapMutations} from "vuex";

    export default {
        name: "PageNavBar",
        data() {
            return {
                modalVisible: false,
                modalButtons: [],
                modalMessage: ''
            }
        },
        computed: {
            ...mapGetters(['mainJSON']),
        },
        methods: {
            ...mapMutations(["push_mainJSON"]),
            exit(){
                this.modalVisible = true
                this.modalButtons = [
                    {value: "Да", status: true},
                    {value: "Нет", status: false}
                ]
                this.modalMessage = 'Ты действительно хочешь выйти?'
            },
            checkAnswer(status){
                this.modalVisible = false
                if(status){
                    this.mainJSON['loginShow'] = true
                    this.mainJSON['mainPageShow'] = false

                    let d = new Date()
                    this.mainJSON.results.dataTimeEnd =  this.mainJSON.results.dataTimeLastUpdate = [
                        d.getFullYear(),
                        ('0' + (d.getMonth() + 1)).slice(-2),
                        ('0' + d.getDate()).slice(-2)
                    ].join('-') + ' ' + [
                        ('0' + (d.getHours())).slice(-2),
                        ('0' + (d.getMinutes())).slice(-2),
                        ('0' + d.getSeconds()).slice(-2)
                    ].join(':');

                    this.push_mainJSON({
                        push: this.mainJSON.mainJSON
                    })

                    localStorage.clear()
                }
            }
        },
        mounted() {
        }
    }
</script>

<style scoped>
    .nav-bar {
        height: 70px;
        background: transparent;
        position: fixed;
        top: 0;
        padding-top: 16px;
        z-index: 99;
    }
</style>