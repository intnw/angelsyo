import { useState, useEffect } from "react";

export default function SearchSuggestionItemView({ searchSuggestion, selectSuggestion }) {
    
    return (
            <p className="w-full p-3 cursor-pointer text-sm hover:text-slate-950 hover:bg-slate-200 
                overflow-clip border-b border-b-slate-300"
                onMouseDown={(e) => selectSuggestion(searchSuggestion)}    
            >
                {searchSuggestion}
            </p>
    );
}