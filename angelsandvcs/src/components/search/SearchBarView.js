import { useState, useEffect } from "react";
import { useSearch } from "../../api/search/useSearch";

import SearchSuggestionItemView  from "./SearchSuggestionItemView";

export default function SearchBarView({ setCurrentSearchQuery }) {
    const [searchQuery, setSearchQuery] = useState();
    const [searchSuggestions, setSearchSuggestions] = useState([]);
    const [showSuggestions, setShowSuggestions] = useState(false);
    const { getSearchSuggestions } = useSearch();

    function selectSuggestion(keyword) {
        const latestQuery = keyword;
        setCurrentSearchQuery(latestQuery);
    }

    function showSearchSuggestions(query) {
        getSearchSuggestions({"query": query})
        .then(jsonResponse => {
            if(jsonResponse.status == 422) {
            }
            else if(jsonResponse.status == 404) {
                // setIsloading(false);
                // setSearchResults([]);
            }
            else if(jsonResponse.ok) {
                setShowSuggestions(true);
                setSearchSuggestions(jsonResponse.data);
            }
        })

    }

    function onEnterPress(e) {
        if(e.keyCode == 13 && e.shiftKey == false) {
            setCurrentSearchQuery(e.target.value.trim());
        }

        setSearchSuggestions([]);
        setShowSuggestions(!showSuggestions);
    }

    function onQueryChange(query) {
        setSearchQuery(query);

        setSearchSuggestions([]);
        setShowSuggestions(!showSuggestions);
        
        showSearchSuggestions(query);
    }

    function onQueryClick(query) {
        setSearchQuery(query);

        setSearchSuggestions([]);
        setShowSuggestions(!showSuggestions);
        
        // showSearchSuggestions(query);
    }
    
    return (
        <div className="flex flex-col w-full justify-center items-center">
            <div className="flex flex-col md:flex-row gap-3 w-full md:max-w-5xl h-fit mt-7 p-3">
                <div className="flex w-fit md:w-1/5 h-fit bg-slate-700 text-white border-2 border-white rounded-full">
                    <p className="p-3 w-fit h-fit text-3xl ">
                        Angels Yo
                    </p>
                </div>
                <div className="relative flex flex-col w-full md:w-3/5 h-fit text-3xl">
                    <div className="relative flex">
                        <input className="w-full h-18 p-3 bg-slate-200 outline-none rounded" type="text"
                            onChange={(e) => onQueryChange(e.target.value)}
                            onKeyDown={onEnterPress}
                            onClick={(e) => onQueryClick(e.target.value)}
                            onBlur={() => setShowSuggestions(false)}
                            value={searchQuery}
                        />
                    </div>

                    {
                        showSuggestions &&
                        <div className="absolute flex w-full mt-[1.9em] text-slate-700 bg-slate-100">
                            <ul className="flex flex-col w-full">
                                {
                                    searchSuggestions.map((searchSuggestion, index) => {
                                        return <SearchSuggestionItemView key={index} 
                                            searchSuggestion={searchSuggestion}
                                            selectSuggestion={selectSuggestion}
                                        />
                                    })
                                }
                            </ul>
                        </div>
                    }
                </div>
                <div className="flex-1 w-full md:w-1/5 h-fit">
                    <input className="w-fit p-3 bg-orange-500 text-3xl text-gray-50 rounded cursor-pointer"
                        type="button"
                        value="Search"
                        onClick={() => setCurrentSearchQuery(searchQuery)}
                    />
                </div>
            </div>
            <div className="text-slate-900">
                <p className="p-3">[search examples: founder, founder united states, vice president india]</p>
            </div>
        </div>
    );
}