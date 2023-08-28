import { useResourceNormalDFS } from '../base/useResourceNormalDFS';

export const useSearch = () => {
    const getReqInfoSearchResults = {"type": "GET", "path": "angel", "authRequired": "no"}
    const getReqInfoSearchResultsByKeyword = {"type": "GET", "path": "angel/search", "authRequired": "no"}
    const getReqInfoSearchResultsByKeywords = {"type": "GET", "path": "angel/search/multikw", "authRequired": "no"}
    const getReqInfoSearchSuggestions = {"type": "GET", "path": "angel-info/suggestions", "authRequired": "no"}

    const [getSearchResults] = useResourceNormalDFS(getReqInfoSearchResults);
    const [getSearchResultsByKeyword] = useResourceNormalDFS(getReqInfoSearchResultsByKeyword);
    const [getSearchResultsByKeywords] = useResourceNormalDFS(getReqInfoSearchResultsByKeywords);
    const [getSearchSuggestions] = useResourceNormalDFS(getReqInfoSearchSuggestions);

    return {
        getSearchResults,
        getSearchResultsByKeyword,
        getSearchResultsByKeywords,
        getSearchSuggestions
    }
};