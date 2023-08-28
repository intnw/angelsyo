export function dictCount(dict) {
    let count = 0;
    for (var key in dict){
        count += dict[key];
    }
    return count;
}

export function getFullName(f, m, l) {
    return [f, m, l].join(" ");
}

export function getFullNameFast(profile) {
    return [profile.first_name, profile.middle_name, profile.last_name].join(" ");
}

export function queryParamsToPath(obj) {
    // ?foo=${encodeURIComponent(data.foo)}&bar=${encodeURIComponent(data.bar)}`
    
    var str = [];
    for (var p in obj)
        if (obj.hasOwnProperty(p)) {
        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
    if(str.length === 0) return "";

    return "?"+str.join("&");
}

// TODO add this when building simply to domain not before thath
export const getOs = () => {
    const os = ['Windows', 'Linux', 'Mac']; // add your OS values
    return navigator.userAgentData.platform;
}

//test timestamps 
//2023-06-08T19:34:47.436959+05:30
//2023-06-09T10:30:23:123465+03:30

const mapMonths = {"01": "Jan", "02": "Feb", "03": "March", "04": "April", "05": "May", "06": "June", 
                    "07": "July", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

//extract infor from time stored in db with TZ active
function getCoolDateTime(time) {
    //2023-06-08T19:34:47.436959+05:30
    const re = /(\d{4})-(\d{2})-(\d{2})+T(\d{2}):(\d{2}).*([\+\-]\d{2}):(\d{2})/;
    const matches = time.match(re);
    return matches;
}

export function getTime(time) {
    const totalLocalOffsetMins = new Date().getTimezoneOffset() / -1;
    const originTime = getCoolDateTime(time);
    const originYear = originTime[1];
    const originMonth = mapMonths[originTime[2]];
    let originDay = originTime[3];
    originDay = originDay[0]==="0"? originDay[1]: originDay;

    const originHours = originTime[4];
    const originMins = originTime[5];
    const originUTCTZHours = originTime[6];
    const originUTCTZMins = originTime[7];
    const localTotalMinsOffset = totalLocalOffsetMins - (parseInt(originUTCTZHours)*60+parseInt(originUTCTZMins));
    const originTotalMins = parseInt(originHours)*60+parseInt(originMins);
    const localTotalMins = originTotalMins + localTotalMinsOffset;
    const localHours = Math.floor(localTotalMins/60);
    const localHoursAMPM = localHours>12? localHours%12 : localHours;
    let localMins = Math.floor(localTotalMins%60);
    localMins = localMins<10? "0"+localMins: localMins;
    const finalLocalTime = localHours>12? localHoursAMPM+":"+localMins+"pm" : localHoursAMPM+":"+localMins+"am";
    const finalLocalDateTime = `${originDay}-${originMonth} ${finalLocalTime}`;
    return finalLocalDateTime; 
}

function nowLocalTime(dateTimeStr) {
    //"2023-06-08T19:34:47.436959+05:30"
    //origin Israel database "2023-06-08T19:34:47.436959+03:30" -> origin epoch -> simple
    //local London machine "-01:30" -> now Epoch
    //local India machine "+05:30" -> now Epoch
    const dateString = dateTimeStr;
    
    let someDate = new Date(dateString);

    const someDateEpoch = someDate.getTime();
    
    const nowEpoch = Date.now();

    const diffEpochMilliSecs = nowEpoch - someDateEpoch; //milli-seconds
    const diffEpochSecs = Math.floor(diffEpochMilliSecs/1000);
    if(Math.floor(diffEpochSecs/60) === 0)  return (diffEpochSecs == "1" )? `${diffEpochSecs} sec`: `${diffEpochSecs} secs`;

    const diffEpochMins = Math.floor(diffEpochSecs/60);
    if(Math.floor(diffEpochMins/60) === 0) return (diffEpochMins == "1" )? `${diffEpochMins} min`: `${diffEpochMins} mins`;

    const diffEpochHours = Math.floor(diffEpochMins/60);
    if(Math.floor(diffEpochHours/24) === 0) return (diffEpochHours == "1" )? `${diffEpochHours} hour`: `${diffEpochHours} hours`;

    const diffEpochDays = Math.floor(diffEpochHours/24);
    if(Math.floor(diffEpochDays/30) === 0) return (diffEpochDays == "1" )? `${diffEpochDays} day`: `${diffEpochDays} days`;

    const diffEpochMonths = Math.floor(diffEpochDays/30);
    if(Math.floor(diffEpochDays/365) === 0) return (diffEpochMonths == "1" )? `${diffEpochMonths} month`: `${diffEpochMonths} months`;

    const diffEpochYears = Math.floor(diffEpochDays/365);
    return `${diffEpochYears} years`;
}

export function getSinceTime(dateTimeStr) {
    const finalLocalDateTime = nowLocalTime(dateTimeStr);
    return finalLocalDateTime; 
}