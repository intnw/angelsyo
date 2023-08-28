import { useState, useEffect } from "react";

import SearchBarView from "./SearchBarView";
import SearchResultsView from "./SearchResultsView";

export default function SearchView() {
    const [currentSearchQuery, setCurrentSearchQuery] = useState("");

    return (
        <div className="flex flex-col items-center w-screen h-fit">
            <SearchBarView setCurrentSearchQuery={setCurrentSearchQuery} />
            <SearchResultsView searchQuery={currentSearchQuery} />
        </div>
    );
}