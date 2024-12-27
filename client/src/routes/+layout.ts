import { showNotification } from "$lib/notification";
import { AuthService, OpenAPI, type Token } from "$lib/openapi";
import { writable } from "svelte/store";

export const prerender = true
export const ssr = false
export const trailingSlash = 'always';

const user = writable<Token|undefined>(undefined);

export const load = async ()=>{
    try {
        const token = (await AuthService.authSession())[0];
        OpenAPI.TOKEN=token.access_token;
        OpenAPI.interceptors.response.use(async (response) => {
            if (!response.ok) {
                const body=await response.json()
                showNotification({title:'Error', kind:'warn', subtitle: body.detail})
            }
            return response
        })
        user.set(token);
        showNotification({title: 'Login Successfull!', kind:'info'})
    } catch(e){
        console.debug("auth error")
        const token=undefined;
    }
    return {user}
}