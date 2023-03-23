import { createWebHistory, createRouter } from "vue-router";
import AuthForm from "@/components/AuthForm";

const routes = [
    {
        path: "/education_system/",
        name: "AuthForm",
        component: AuthForm,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;