import { createWebHistory, createRouter } from "vue-router";
import UsersPage from "@/components/UsersPage";

const routes = [
    {
        path: "/",
        name: "UsersPage",
        component: UsersPage,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;