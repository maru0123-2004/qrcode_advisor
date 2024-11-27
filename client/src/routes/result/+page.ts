import type { PageLoad } from "./$types";

export const load:PageLoad=({url})=>{
    return {
        destId:url.searchParams.get("dest_id"),
        qrdata:url.searchParams.get("qrdata"),
    }
}