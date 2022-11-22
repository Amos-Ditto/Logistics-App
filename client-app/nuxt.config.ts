import presetIcons from '@unocss/preset-icons';

export default defineNuxtConfig({
    css: ['~/assets/css/tailwind.css'],
    modules: ['@nuxtjs/tailwindcss', '@nuxtjs/color-mode', '@pinia/nuxt', '@unocss/nuxt'],
    app: {
        head: {
            charset: 'utf-16',
            viewport: 'width=500, initial-scale=1',
            title: 'Logistics',
            meta: [{ name: 'description', content: 'Send & Fetch products throughout any place.' }],
        },
        pageTransition: { name: 'page', mode: 'out-in' },
        layoutTransition: { name: 'layout', mode: 'out-in' },
    },
    unocss: {
        icons: true,
        presets: [presetIcons({})],
    },
    colorMode: {
        classSuffix: '',
    },
    routeRules: {
        '/maps/**': { ssr: false },
    },
});
