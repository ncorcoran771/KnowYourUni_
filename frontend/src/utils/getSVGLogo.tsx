/* Helper function to return the re-colored SVG image, according to the logo */

import { theme } from "antd";
import logo from "../assets/logo.svg";

export const SVGLogo = () => {
    const { token } = theme.useToken();

    return (
        <img
        src={logo}
        alt="logo"
        style={{
            height: 40,
            fill: token.colorPrimary, 
        }}
        />
    );
}