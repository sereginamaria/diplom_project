<template>
    <div v-if="show" class="dialog">
        <div class="dialog-content">
            <div class="mb-3">
                <slot></slot>
            </div>
            <MyButton v-for="button in buttons" :key="button.value"  @click="$emit('update', button.status)"
                      class="me-3 blue-buttons"
            >
                {{button.value}}
            </MyButton>
        </div>
    </div>
</template>

<script>
    export default {
        name: "MyModal",
        props: {
            show: {
                type: Boolean
            },
            buttons: {},
            answer: {}
        },
        methods: {
            checkAnswer(status){
                this.$emit('update:answer', status)
            }
        }
    }
</script>

<style scoped>
</style>