<template>
    <nav class="px-2 md:px-12 lg:px-0 w-full lg:w-[1100px] flex flex-col py-1 sm:py-2">
        <div class="w-full flex flex-row justify-between items-center py-4 px-2 sm:px-0">
            <div class="left-menu flex flex-row items-center">
                <IconsMenuIcon class="hover:scale-105 transition duration-200 cursor-pointer" />
            </div>
            <div class="right flex flex-row gap-x-8 sm:gap-x-16 items-center justify-center">
                <div
                    class="notification relative flex flex-row items-center justify-center cursor-pointer p-2 hover:bg-gray-200 rounded-full transition duration-200"
                >
                    <div class="i-carbon-notification text-2xl"></div>
                </div>
                <div class="account bg-emerald-100 rounded-full cursor-pointer">
                    <img src="@/assets/images/profile-min.svg" alt="Account" class="w-8 h-8" />
                </div>
            </div>
        </div>
    </nav>
</template>
