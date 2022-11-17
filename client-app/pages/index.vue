<template>
    <section class="h-full flex flex-col items-center justify-start">
        <div class="body w-[360px] flex items-start justify-center flex-col pb-4 pt-12">
            <div class="banner w-full flex items-center justify-center">
                <img src="@/assets/images/Banner.svg" alt="" />
            </div>
            <div class="title-text pt-20">
                <h3 class="text-3xl tracking-wide text-dark capitalize">
                    send anything <span class="font-bold text-[#0C3A30]">fast</span>
                </h3>
            </div>
            <article class="pt-4 indent-8 leading-6 text-gray-600 tracking-wide font-light text-lg">
                Create your quick account, find the best rates and transfer your items from one location to another.
            </article>
            <div class="redirect pt-16 w-full flex items-center justify-center">
                <button
                    class="bg-[#0C3A30] border-8 border-[#c6d1ce] hover:border-[#95bfb2] rounded-full p-3 text-gray-50 transition duration-200"
                >
                    <div class="i-carbon-arrow-up-right text-3xl cursor-pointer transition duration-200"></div>
                </button>
            </div>
        </div>
    </section>
</template>

<style scoped>
.redirect button:hover .i-carbon-arrow-up-right {
    @apply translate-x-0.5 -translate-y-0.5;
}
</style>
