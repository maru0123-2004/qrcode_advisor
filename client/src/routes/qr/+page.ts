import { redirect } from "@sveltejs/kit";
import type { PageLoad } from "./$types";

export const load:PageLoad=({url})=>{
    const dest_id=url.searchParams.get("dest_id")
    if(!dest_id){
        throw redirect(300, "/")
    }
    return { dest_id }
}