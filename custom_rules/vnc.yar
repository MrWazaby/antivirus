rule UltraVNC
{
    strings:
        $name = "UltraVNC" nocase wide

    condition:
        $name
}
