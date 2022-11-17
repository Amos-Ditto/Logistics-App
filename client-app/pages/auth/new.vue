<template>
    <section class="flex items-center justify-center flex-col pb-4 w-full">
        <div class="body w-full sm:w-[480px] h-[800px] flex flex-col py-8 z-20 px-4">
            <div class="title flex flex-col gap-y-2">
                <h3 class="text-dark text-2xl tracking-wide font-light">Create a Free</h3>
                <h4 class="tracking-wide text-5xl text-default font-normal">Account</h4>
            </div>
            <form @submit.prevent="" class="flex flex-col gap-y-5 w-full pt-8 px-2">
                <div class="input-field w-full flex flex-col gap-y-1">
                    <label for="name">FullName</label>
                    <div class="input relative w-full flex items-center">
                        <input type="text" id="name" />
                        <div class="i-carbon-user absolute right-4 text-2xl"></div>
                    </div>
                </div>
                <div class="input-field w-full flex flex-col gap-y-1">
                    <label for="mail">Email Address</label>
                    <div class="input relative w-full flex items-center">
                        <input type="email" id="mail" />
                        <div class="i-carbon-email absolute right-4 text-2xl"></div>
                    </div>
                </div>
                <div class="input-field w-full flex flex-col gap-y-1">
                    <label for="pass">Password</label>
                    <div class="input relative w-full flex items-center">
                        <input type="password" id="pass" />
                        <div class="i-carbon-password absolute right-4 text-2xl"></div>
                    </div>
                </div>
                <div class="submit pt-4 w-full flex items-center justify-center">
                    <button
                        class="bg-[#0C3A30] w-full py-3 px-3 flex flex-row items-center justify-center gap-x-3 text-gray-50 rounded hover:opacity-90 transition duration-200"
                    >
                        <span class="tracking-wide capitalize text-lg font-semibold">Sign Up</span>
                        <!-- <div class="i-carbon-arrow-up-right text-3xl cursor-pointer transition duration-200"></div> -->
                    </button>
                </div>
            </form>
            <div id="gSignInWrapper" class="flex flex-row justify-center gap-x-4 w-full items-center pb-4 pt-12 px-2">
                <span class="label">Sign in with:</span>
                <button class="hover:opacity-80 transition duration-200">
                    <img src="@/assets/images/btn_google.png" alt="" />
                </button>
            </div>
            <div class="other flex flex-col w-full items-center py-6">
                <small class="text-xl font-serif"
                    >Exiting User?
                    <NuxtLink to="/auth" class="font-semibold tracking-wide text-default px-1 hover:opacity-80 cursor-pointer"
                        >Login</NuxtLink
                    ></small
                >
            </div>
        </div>
    </section>
</template>

<style scoped>
.input-field label {
    @apply text-base tracking-wide;
}
.input-field input {
    @apply w-full py-3 px-4 rounded-md border border-default outline-none bg-inherit tracking-wide;
}
.submit button:hover .i-carbon-arrow-up-right {
    @apply translate-x-0.5 -translate-y-0.5;
}

span.label {
    font-family: serif;
    font-weight: normal;
}
</style>
