import Vuex from 'vuex'
import axios from "axios";

import date from "./date"

export default new Vuex.Store({
    state: {
        mainJSON: {},
    },
    actions: {
        get_mainJSON({commit}){
            if (!localStorage.login && !localStorage.hash) {
                commit('set_mainJSON', date.date)
            }
            else {
                axios.post( "/city_literacy/server_request/auth_city.php", {
                    login: localStorage.login,
                    hash: localStorage.hash
                })
                    .then(function (response) {
                        if (response.data.status === "ok") {
                            commit('set_mainJSON', JSON.parse(response.data.json))
                        }
                        if (response.data.status === "error") {
                            localStorage.clear()
                            window.location.reload();
                            commit('set_mainJSON', date.date)
                        }
                    })
                    .catch(function () {
                    })
            }
        }
    },
    mutations: {
        set_mainJSON: (state, el) => {
            state.mainJSON = el
        },
        push_mainJSON: (state, push) => {
            if (localStorage.login && localStorage.hash){
                axios.post( "/city_literacy/server_request/receiver.php", {
                    mainJSON: push.push
                })
                    .then(function () {

                     /*   Vue.set(state, "responsePushJSON", response.data)*/

                    })
                    .catch(function () {
     /*                   Vue.set(state, "responsePushJSON", "noInternet")*/
                    })
            }
            else {

                window.location.reload();
            }
        },
    },
    getters: {
        mainJSON(state){
            return state.mainJSON;
        },
    },
})

