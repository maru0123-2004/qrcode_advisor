import type { PageLoad } from "./$types";

export const load:PageLoad=({url})=>{
    return {
        stop_id: url.searchParams.get("stop_id")
    }
}