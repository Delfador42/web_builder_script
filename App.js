import * as React from "react";
  import { Route, Routes, Link } from "react-router-dom";
  import { routes } from './components/Routes'
   var filename =['', 'a.pdf', 'c.pdf', 'b.pdf', 'q.pdf'] ; 
export default function App() {
  return (
    <div>
      <Link className="site-title" to="/">Site Title</Link>
    <div className="wrapper">
      <div className="sidebar">
        <ul className="nav">

<li><Link to="Page1">{filename[1]}</Link></li>
<li><Link to="Page2">{filename[2]}</Link></li>
<li><Link to="Page3">{filename[3]}</Link></li>
<li><Link to="Page4">{filename[4]}</Link></li>
        </ul>
        <Routes>
          {routes.map(({ path }) => (
            <Route key={path} path={path}  />
          ))}
        </Routes>
      </div>

      <Routes>
        {routes.map(({ path, main }) => (
          <Route key={path} path={path} element={main()} />
        ))}
      </Routes>
    </div>

    </div>
  );
}
