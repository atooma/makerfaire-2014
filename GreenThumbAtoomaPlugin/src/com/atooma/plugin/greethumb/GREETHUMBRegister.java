
package com.atooma.plugin.greethumb;

import com.atooma.plugin.Module;
import com.atooma.sdk.RegisterService;

public class GREETHUMBRegister extends RegisterService {
    @Override
    public Module getModuleInstance() {
        return new GREETHUMB(this, GREETHUMB.MODULE_ID, GREETHUMB.MODULE_VERSION);
    }
}
