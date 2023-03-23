<template>
    <div class="background-body">
        <PageNavBar/>
    </div>
</template>

<script>
    import PageNavBar from "@/components/PageNavBar";
    import {mapGetters} from "vuex";
    export default {
        name: "PageBody",
        components: {PageNavBar},
        computed: {
            ...mapGetters(['mainJSON']),
        },
    }
</script>

<style scoped>
    .background-body {
        height: 100vh;
        background: linear-gradient(360deg, rgba(42, 148, 214, 0.8) 62.67%, rgba(52, 74, 95, 0.8) 99.29%), url("../assets/Background.svg") no-repeat center center fixed;
        background-size: cover;
        backdrop-filter: blur(2.71828px);
    }
</style>