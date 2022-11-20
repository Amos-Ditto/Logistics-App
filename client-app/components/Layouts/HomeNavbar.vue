<script setup lang="ts">
const authenticated = ref<boolean>(false);
</script>
<template>
    <nav class="px-2 md:px-12 lg:px-0 w-full lg:w-[1100px] flex flex-col py-1 sm:py-2">
        <div class="w-full flex flex-row justify-between items-center py-4 px-2 sm:px-0">
            <div class="left-menu flex flex-row items-center">
                <IconsMenuIcon class="hover:scale-105 transition duration-200 cursor-pointer" />
            </div>
            <div class="right flex flex-row gap-x-4 sm:gap-x-8 items-center justify-center">
                <div
                    class="notification relative flex flex-row items-center justify-center cursor-pointer p-2 hover:bg-gray-200 rounded-full transition duration-200"
                >
                    <div class="i-carbon-notification text-2xl"></div>
                </div>
                <div class="account">
                    <Transition mode="out-in">
                        <div v-if="authenticated">
                            <button
                                class="text-base tracking-wide px-3 py-1 border-default hover:opacity-70 focus:opacity-70 transition duration-200"
                            >
                                Logout
                            </button>
                        </div>
                        <div class="new flex flex-row items-center gap-x-3" v-else>
                            <button
                                @click="useRouter().push('/auth')"
                                class="text-base tracking-wide px-3 py-1 border-default hover:opacity-70 focus:opacity-70 transition duration-200"
                            >
                                Login
                            </button>
                            <button
                                @click="useRouter().push('/auth/new')"
                                class="border border-default rounded-md text-gray-200 bg-default text-base tracking-wide px-3 py-1 hover:opacity-70 focus:opacity-70 transition duration-200"
                            >
                                Sign Up
                            </button>
                        </div>
                    </Transition>
                </div>
            </div>
        </div>
    </nav>
</template>
