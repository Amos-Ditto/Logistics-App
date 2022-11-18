<script setup lang="ts">
definePageMeta({
    layout: false,
})
</script>
<template>
    <main class="w-full flex flex-col">
        <NuxtLayout name="home">
            <header class="flex flex-row py-2 px-4 gap-x-2 items-center justify-start mt-2">
                <button class="bg-default text-gray-50">send</button>
                <button>fetch</button>
                <button>ride</button>
            </header>
            <section class="w-full flex flex-col px-4 pt-7 pb-4 gap-y-4 md:gap-y-10">
                <div class="locations flex flex-col w-full gap-y-2">
                    <h3 class="font-bold text-lg tracking-wide">Details</h3>
                    <div class="flex flex-col gap-y-2 gap-x-2 md:grid grid-cols-2">
                        <div class="from-details flex flex-col py-2 w-[90%] md:w-[84%]">
                            <button
                                class="py-3 px-2.5 rounded-xl flex flex-row items-center justify-between border border-default hover:border-emerald-600 focus:border-emerald-600 transition duration-200"
                            >
                                <div class="name flex flex-row items-center gap-x-3">
                                    <div class="icon"><img src="@/assets/images/current-location.svg" alt="" /></div>
                                    <div class="text flex flex-col">
                                        <span class="text-sm tracking-wide text-neutral-500">Enter picking point</span>
                                    </div>
                                </div>
                                <div class="redirect">
                                    <div class="i-carbon-chevron-right text-xl"></div>
                                </div>
                            </button>
                        </div>
                        <div class="to-details flex flex-col py-2 w-[90%] md:w-[84%]">
                            <button
                                class="py-3 px-2.5 rounded-xl flex flex-row items-center justify-between border border-default hover:border-emerald-600 focus:border-emerald-600 transition duration-200"
                            >
                                <div class="name flex flex-row items-center gap-x-3">
                                    <div class="icon"><img src="@/assets/images/map-pin.svg" alt="" /></div>
                                    <div class="text flex flex-col">
                                        <span class="text-sm tracking-wide text-neutral-500">Enter receiver destination</span>
                                    </div>
                                </div>
                                <div class="redirect">
                                    <div class="i-carbon-chevron-right text-xl"></div>
                                </div>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="pickup-details flex flex-col w-full gap-y-6 md:gap-y-3">
                    <h3 class="font-bold text-lg tracking-wide">PickUp</h3>
                    <div class="w-full flex flex-col md:grid grid-cols-2 gap-x-4 gap-y-8 md:gap-y-4">
                        <div class="time w-[90%] md:w-[84%] grid grid-cols-3 items-center gap-x-3">
                            <h3 class="font-light text-base tracking-wide">Time:</h3>
                            <div class="time-label flex flex-row justify-start items-center">
                                <div class="label-container border border-default flex flex-row gap-x-0.5 rounded-full">
                                    <button class="tracking-wide rounded-full bg-default text-gray-50 text-sm px-4 py-1.5">AM</button>
                                    <button class="tracking-wide rounded-full text-default text-sm px-4 py-1.5">PM</button>
                                </div>
                            </div>
                            <div class="time-list flex flex-row items-center justify-center">
                                <button class="flex flex-row gap-x-2 rounded-full px-3 py-1.5 border border-default">
                                    <span>10:00</span>
                                    <span>-</span>
                                    <span>12:00</span>
                                </button>
                            </div>
                        </div>
                        <div class="date w-[90%] md:w-[84%] grid grid-cols-2 items-center gap-x-3">
                            <h3>Date:</h3>
                            <div class="date-label flex flex-row items-center justify-end">
                                <button class="rounded-full border border-default px-4 py-1.5">
                                    <span class="text-base tracking-wide capitalize">today</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="description flex flex-col gap-y-4 w-full">
                    <h3 class="text-lg font-bold tracking-wide capitalize">item description</h3>
                    <div class="description-list grid grid-cols-3 md:grid-cols-4 gap-x-3 md:gap-x-6 gap-y-6 md:gap-y-7">
                        <button>food</button>
                        <button>documents</button>
                        <button>clothings</button>
                        <button>digital products</button>
                        <button>books</button>
                        <button>liquids</button>
                        <button>add more</button>
                    </div>
                </div>
                <div class="price flex flex-row justify-between items-center pt-6 pb-4">
                    <h4 class="text-lg font-semibold tracking-wide">Total Price:</h4>
                    <div class="amount flex flex-row gap-x-0.5">
                        <span>$</span>
                        <span>560</span>
                    </div>
                </div>
                <div class="send-order w-full flex flex-col items-center justify-center gap-y-2">
                    <button
                        class="bg-[#0C3A30] border-8 border-[#c6d1ce] hover:border-[#95bfb2] rounded-full p-3 text-gray-50 transition duration-200"
                    >
                        <div class="i-carbon-arrow-up-right text-3xl cursor-pointer transition duration-200"></div>
                    </button>
                    <h4 class="text-xl tracking-wide uppercase font-light">send order</h4>
                </div>
            </section>
        </NuxtLayout>
    </main>
</template>

<style scoped>
header button {
    @apply px-6 py-1 md:py-2 rounded-xl border border-transparent hover:border-default tracking-wide text-base font-light capitalize transition duration-200;
}

.time-list span {
    @apply text-base text-default tracking-wide;
}

.description-list button {
    @apply px-4 py-1.5 bg-default opacity-60 hover:opacity-100 focus:opacity-100 rounded-full text-gray-50 tracking-wide capitalize text-sm md:text-base transition duration-200;
}

.amount span {
    @apply text-lg tracking-wide font-light;
}

.send-order button:hover .i-carbon-arrow-up-right {
    @apply translate-x-0.5 -translate-y-0.5;
}
</style>
