import { createRouter, createWebHistory } from "vue-router";

const Wallet = () => import('@/components/Wallet.vue')
const Assets = () => import('@/components/Assets.vue')

const routes = [
    {
        path: '/',
        name: 'Wallet',
        component: Wallet
    },
    {
        path: '/assets',
        name: 'Assets',
        component: Assets
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router