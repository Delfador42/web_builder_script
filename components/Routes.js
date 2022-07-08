import Home from "../pages/Home" 
import Page1 from "../pages/Page1";
import Page2 from "../pages/Page2";
import Page3 from "../pages/Page3";
import Page4 from "../pages/Page4";
export const routes = [
{path: "/",main: () => <Home />,},
{path: "/Page1",main: () => <Page1 />,}, 
{path: "/Page2",main: () => <Page2 />,}, 
{path: "/Page3",main: () => <Page3 />,}, 
{path: "/Page4",main: () => <Page4 />,}, 
];