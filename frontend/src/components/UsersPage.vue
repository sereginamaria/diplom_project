<template>
    <div class="container">
        Прикол
        <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'UsersPage',
        data() {
            return {
                msg: '',
            };
        },
        methods: {
            getMessage() {
                const path = 'http://localhost:8060/users';
                axios.get(path)
                    .then((res) => {
                        this.msg = res.data;
                    })
                    .catch((error) => {
                        // eslint-выключение следующей строки
                        console.error(error);
                    });
            },
        },
        created() {
            this.getMessage();
        },
    };
</script>