<template>
    <div class="container-fluid d-flex justify-content-between align-items-center footer">
        <div v-if="this.mainJSON.task1Show">
            <MyButton class="ml-3 transparent-buttons"
                      data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Браузер"
                      @click="openBrowser"
            >
                <img src="../assets/iconBrowser.svg">
            </MyButton>
            <MyButton  class="ml-3 transparent-buttons"
                       data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Планировщик задач"
                       @click="openTaskManager"
            >
                <img src="../assets/iconTaskManager.svg">
            </MyButton>
        </div>
        <div v-if="this.mainJSON.task2Show">
            <MyButton class="ml-3 transparent-buttons"
                      data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Чат"
                      @click="openChat"
            >
                <img src="../assets/tak2-chat-icon.svg">
            </MyButton>
        </div>
        <div v-if="this.mainJSON.task3Show">
            <MyButton class="ml-3 transparent-buttons"
                      data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Браузер"
                      @click="openBrowser"
            >
                <img src="../assets/iconBrowser.svg">
            </MyButton>
            <MyButton  class="ml-3 transparent-buttons"
                       data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Планировщик задач"
                       @click="openTaskManager"
            >
                <img src="../assets/iconTaskManager.svg">
            </MyButton>
            <MyButton  class="ml-3 transparent-buttons"
                       data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Планировщик задач"
                       @click="openMap"
            >
                <img src="../assets/task3-map.svg">
            </MyButton>
            <MyButton  class="ml-3 transparent-buttons"
                       data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Планировщик задач"
                       @click="openBooklet"
            >
                <img src="../assets/task3-presentation.svg">
            </MyButton>
            <MyButton  class="ml-3 transparent-buttons"
                       data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Планировщик задач"
                       @click="openChat"
            >
                <img src="../assets/tak2-chat-icon.svg">
            </MyButton>
        </div>
        <MyButton style="background: #F3AE4E; border-color: #F3AE4E; width: 200px" @click="showModal">Завершить</MyButton>
    </div>

    <MyModal v-model:show="modalVisible" v-model:buttons="modalButtons"
             @update="checkAnswer"
    >
        {{this.modalMessage}}
    </MyModal>

</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "PageFooter",
        computed: {
            ...mapGetters(['mainJSON']),
        },
        data() {
            return {
                modalVisible: false,
                modalButtons: [],
                modalMessage: ''
            }
        },
        methods: {
            openBrowser(){
                if(this.mainJSON.task1Show){
                    this.mainJSON.task1.browserShow = !this.mainJSON.task1.browserShow
                }
                if(this.mainJSON.task3Show){
                    this.mainJSON.task3.browserShow = !this.mainJSON.task3.browserShow
                }
            },
            openTaskManager(){
                if(this.mainJSON.task1Show){
                    this.mainJSON.task1.taskManagerShow = !this.mainJSON.task1.taskManagerShow
                }
                if(this.mainJSON.task3Show){
                    this.mainJSON.task3.taskManagerShow = !this.mainJSON.task3.taskManagerShow
                }
            },
            openChat(){
                if(this.mainJSON.task2Show){
                    this.mainJSON.task2.chatShow = !this.mainJSON.task2.chatShow
                }
                if(this.mainJSON.task3Show){
                    this.mainJSON.task3.chatShow = !this.mainJSON.task3.chatShow
                }
            },
            openBooklet(){
                this.mainJSON.task3.bookletShow = !this.mainJSON.task3.bookletShow
            },
            openMap(){
                this.mainJSON.task3.mapObjectsShow = !this.mainJSON.task3.mapObjectsShow
            },
            showModal(){
                this.modalVisible = true
                this.modalButtons = [
                    {value: "Да", status: true},
                    {value: "Нет", status: false}
                ]
                this.modalMessage = 'Ты действительно хочешь завершить задание  перейти к следующему?'
            },
            checkAnswer(){
                this.modalVisible = false
                let change = 0
                if(this.mainJSON.task1Show && change === 0){
                    this.mainJSON["task1Show"] = false
                    this.mainJSON["task2Show"] = true
                    this.mainJSON["instructionShow"] = true
                    this.mainJSON["mainPageShow"] = false
                    change++
                }
                if(this.mainJSON.task2Show  && change === 0){
                    this.mainJSON["task2Show"] = false
                    this.mainJSON["task3Show"] = true
                    this.mainJSON["instructionShow"] = true
                    this.mainJSON["mainPageShow"] = false
                    change++
                }
                if(this.mainJSON.task3Show  && change === 0){
                    this.mainJSON["task2Show"] = false
                    this.mainJSON["task3Show"] = true
                    this.mainJSON["instructionShow"] = true
                    this.mainJSON["mainPageShow"] = false
                }
            }
        }
    }
</script>

<style scoped>
    .footer {
        height: 72px;
        background: #344A5F;
        backdrop-filter: blur(8.15485px);
        position: fixed;
        bottom: 0;
        z-index: 99;
    }

</style>