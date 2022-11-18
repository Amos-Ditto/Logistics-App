<template>
    <nav class="w-full flex flex-row justify-between items-center py-4 px-2 sm:px-0">
        <div class="left-menu">
            <div class="i-carbon-menu text-2xl"></div>
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
    </nav>
</template>
